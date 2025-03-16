const fs = require("fs");
const { OpenAI } = require("openai");
const { encode } = require("gpt-tokenizer");
require("dotenv").config();

// Initialize OpenAI API client
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

// Function to split text into chunks
function splitIntoChunks(text, maxChunkSize = 1000, overlap = 100) {
  const sentences = text.match(/[^.!?]+[.!?]+/g) || [];
  const chunks = [];
  let currentChunk = "";

  for (const sentence of sentences) {
    if (
      (currentChunk + sentence).length > maxChunkSize &&
      currentChunk.length > 0
    ) {
      chunks.push(currentChunk);
      // Keep some overlap for context continuity
      const lastSentences = currentChunk
        .split(/[.!?]+\s+/)
        .slice(-3)
        .join(". ");
      currentChunk = lastSentences + " " + sentence;
    } else {
      currentChunk += (currentChunk ? " " : "") + sentence;
    }
  }

  if (currentChunk.length > 0) {
    chunks.push(currentChunk);
  }

  return chunks;
}

// Function to create embeddings for text chunks
async function createEmbeddings(chunks) {
  const embeddings = [];

  // Process in batches to avoid rate limits
  for (let i = 0; i < chunks.length; i++) {
    try {
      const response = await openai.embeddings.create({
        model: "text-embedding-ada-002",
        input: chunks[i],
      });
      embeddings.push({
        text: chunks[i],
        embedding: response.data[0].embedding,
      });
    } catch (error) {
      console.error(`Error creating embedding for chunk ${i}:`, error);
    }

    // Add small delay between requests
    if (i < chunks.length - 1) {
      await new Promise((resolve) => setTimeout(resolve, 200));
    }
  }

  return embeddings;
}

// Function to get embedding for a query
async function getQueryEmbedding(query) {
  try {
    const response = await openai.embeddings.create({
      model: "text-embedding-ada-002",
      input: query,
    });
    return response.data[0].embedding;
  } catch (error) {
    console.error("Error creating query embedding:", error);
    throw error;
  }
}

// Calculate cosine similarity between two vectors
function cosineSimilarity(vecA, vecB) {
  const dotProduct = vecA.reduce((sum, val, i) => sum + val * vecB[i], 0);
  const magA = Math.sqrt(vecA.reduce((sum, val) => sum + val * val, 0));
  const magB = Math.sqrt(vecB.reduce((sum, val) => sum + val * val, 0));
  return dotProduct / (magA * magB);
}

// Find most relevant chunks based on similarity to query
function findRelevantChunks(queryEmbedding, documentEmbeddings, topK = 3) {
  const similarities = documentEmbeddings.map((item) => ({
    text: item.text,
    similarity: cosineSimilarity(queryEmbedding, item.embedding),
  }));

  return similarities
    .sort((a, b) => b.similarity - a.similarity)
    .slice(0, topK);
}

// Generate response using the retrieved context
async function generateResponseWithContext(query, relevantChunks) {
  // Calculate token count to avoid exceeding model limits
  const contextText = relevantChunks.map((chunk) => chunk.text).join("\n\n");
  const tokenCount = encode(contextText).length;

  console.log("Token Count: ", tokenCount);

  const systemPrompt = `You are a helpful assistant that provides accurate information based on the given context.
    If the answer cannot be found in the context, acknowledge that you don't have enough information.`;

  try {
    const response = await openai.chat.completions.create({
      model: "gpt-4o-mini", // Use the latest model
      messages: [
        { role: "system", content: systemPrompt },
        {
          role: "user",
          content: `Context information is below.
            ---------------------
            ${contextText}
            ---------------------
            Given this context, please answer the following question: ${query}
            Provide a comprehensive and accurate response based only on the information in the context.
          `,
        },
      ],
      temperature: 0.3, // Lower temperature for more accurate answers
    });

    return response.choices[0].message.content;
  } catch (error) {
    console.error("Error generating response:", error);
    throw error;
  }
}

// Process a file and cache embeddings
async function processAndCacheFile(filePath) {
  console.log(`Processing and caching file: ${filePath}`);
  const fileContent = fs.readFileSync(filePath, "utf-8");
  const chunks = splitIntoChunks(fileContent);
  const embeddings = await createEmbeddings(chunks);

  // Cache embeddings to avoid recomputing
  const cacheDir = "./cache";
  if (!fs.existsSync(cacheDir)) {
    fs.mkdirSync(cacheDir);
  }

  const fileName = filePath
    .split("/")
    .pop()
    .replace(/\.[^/.]+$/, "");
  fs.writeFileSync(
    `${cacheDir}/${fileName}_embeddings.json`,
    JSON.stringify(embeddings)
  );

  return embeddings;
}

// Get embeddings from cache or compute them
async function getEmbeddings(filePath) {
  const fileName = filePath
    .split("/")
    .pop()
    .replace(/\.[^/.]+$/, "");
  const cachePath = `./cache/${fileName}_embeddings.json`;

  try {
    if (fs.existsSync(cachePath)) {
      console.log("Using cached embeddings");
      return JSON.parse(fs.readFileSync(cachePath, "utf-8"));
    } else {
      return await processAndCacheFile(filePath);
    }
  } catch (error) {
    console.error("Error getting embeddings:", error);
    return await processAndCacheFile(filePath);
  }
}

// Main RAG function
async function runRAG(filePath, query) {
  try {
    console.log(`Processing query: "${query}"`);

    // Get document embeddings
    const documentEmbeddings = await getEmbeddings(filePath);

    // Get query embedding
    const queryEmbedding = await getQueryEmbedding(query);

    // Find relevant chunks
    const relevantChunks = findRelevantChunks(
      queryEmbedding,
      documentEmbeddings
    );

    console.log(`Found ${relevantChunks.length} relevant chunks`);

    // Generate response
    const response = await generateResponseWithContext(query, relevantChunks);

    console.log("\n--- Generated Response ---");
    console.log(response);

    return response;
  } catch (error) {
    console.error("Error running RAG:", error);
  }
}

// Export functions for use in other modules
module.exports = {
  runRAG,
  processAndCacheFile,
};

// Run the RAG system if this file is executed directly
if (require.main === module) {
  const filePath = process.argv[2] || "sample_blog.txt";
  const query = process.argv[3] || "What is RAG?";

  console.log(`Reading file: ${filePath}`);
  console.log(`Query: "${query}"`);

  runRAG(filePath, query);
}
