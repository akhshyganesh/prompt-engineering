// Import required libraries
const fs = require("fs");
const { OpenAI } = require("openai");
const _ = require("lodash");

// Initialize OpenAI API client
const openai = new OpenAI({
  apiKey: "",
});

// Function to read the content of a local file
function readLocalFile(filePath) {
  return fs.readFileSync(filePath, "utf-8");
}

// Function to retrieve relevant content from the file based on a query
function retrieveRelevantContent(query, text) {
  const lowerCaseText = text.toLowerCase();
  const lowerCaseQuery = query.toLowerCase();

  const lines = text.split("\n");
  const relevantLines = lines.filter((line) =>
    line.toLowerCase().includes(lowerCaseQuery)
  );
  return relevantLines.join("\n");
}

// Function to interact with OpenAI's model using retrieved content
async function generateResponseWithContext(query, content) {
  const prompt = `
    Use the following context to answer the user's question:
    ${content}

    User's Question: ${query}
  `;

  try {
    const response = await openai.chat.completions.create({
      model: "gpt-4", // Or gpt-3.5-turbo
      messages: [
        { role: "system", content: "You are a helpful assistant." },
        { role: "user", content: prompt },
      ],
    });
    return response.choices[0].message.content;
  } catch (error) {
    console.error("Error generating response:", error);
  }
}

// Main logic to read the file, retrieve relevant content, and generate a response
async function runRAG(filePath, query) {
  const fileContent = readLocalFile(filePath);
  const relevantContent = retrieveRelevantContent(query, fileContent);
  const response = await generateResponseWithContext(query, relevantContent);
  console.log("Generated Response:", response);
}

// Test the RAG system with a sample blog file and query
const filePath = "sample_blog.txt"; // Path to your local text file
const query = "What is RAG?";

runRAG(filePath, query);
