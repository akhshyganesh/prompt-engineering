# 🎯 Types of Prompts: A Comprehensive Guide

Understanding different types of prompts is crucial for effective prompt engineering. Each type serves specific purposes and produces different kinds of outputs. This guide covers all major prompt types with practical examples and use cases.

## 📚 Classification Overview

### By Function
1. **Instructional Prompts** - Direct commands
2. **Interrogative Prompts** - Questions seeking information
3. **Completion Prompts** - Partial text requiring completion
4. **Conversational Prompts** - Dialogue-based interactions
5. **Creative Prompts** - Artistic and imaginative tasks
6. **Analytical Prompts** - Analysis and reasoning tasks

### By Structure
1. **Zero-shot Prompts** - No examples provided
2. **One-shot Prompts** - Single example provided
3. **Few-shot Prompts** - Multiple examples provided
4. **Chain-of-Thought Prompts** - Step-by-step reasoning

### By Complexity
1. **Simple Prompts** - Single, direct requests
2. **Complex Prompts** - Multi-part, detailed requests
3. **Compound Prompts** - Multiple related tasks
4. **Nested Prompts** - Hierarchical task structure

## 🎯 Instructional Prompts

Direct commands that tell the AI what to do.

### Basic Structure
```
[Action Verb] + [Object/Topic] + [Specific Requirements]
```

### Examples

#### ✅ Simple Instructions
```
"Explain quantum computing in simple terms."
```

#### ✅ Detailed Instructions
```
"Write a 300-word blog post about renewable energy benefits. Include statistics, use a conversational tone, and target homeowners considering solar panels."
```

#### ✅ Multi-step Instructions
```
"Create a workout plan by:
1. Assessing fitness goals for weight loss
2. Designing a 4-week schedule
3. Including both cardio and strength training
4. Providing progression guidelines
5. Adding nutrition recommendations"
```

### Best Practices
- Use clear action verbs (write, explain, create, analyze)
- Specify output format and length
- Include context and constraints
- Define the target audience

### Common Use Cases
- Content creation
- Code generation
- Data analysis
- Process documentation
- Educational materials

## ❓ Interrogative Prompts

Questions designed to extract specific information.

### Question Types

#### 🔍 Open-ended Questions
```
"What are the implications of artificial intelligence on future employment?"
```

#### 🎯 Specific Questions
```
"How many parameters does GPT-4 have?"
```

#### 🤔 Analytical Questions
```
"Why did the Roman Empire fall, and what lessons can modern societies learn?"
```

#### 📊 Comparative Questions
```
"What are the key differences between React and Vue.js for web development?"
```

### Question Frameworks

#### The 5W+H Framework
```
"Who are the key stakeholders in cloud migration?
What are the main challenges they face?
When is the best time to migrate?
Where should the migration start?
Why is cloud migration important?
How can organizations ensure successful migration?"
```

#### Socratic Questioning
```
"What assumptions are we making about user behavior?
What evidence supports these assumptions?
What if these assumptions are wrong?
How might users actually behave differently?
What would change our approach?"
```

### Best Practices
- Be specific about what information you need
- Use appropriate question words (what, how, why, when, where, who)
- Provide context for complex questions
- Break down complex questions into simpler parts

## 🔄 Completion Prompts

Partial text that requires completion or continuation.

### Types of Completion

#### ✏️ Sentence Completion
```
"The three main principles of good user interface design are..."
```

#### 📝 Paragraph Completion
```
"Artificial intelligence is transforming healthcare in unprecedented ways. From diagnostic imaging to personalized treatment plans, AI is..."
```

#### 📋 List Completion
```
"Essential skills for a data scientist include:
1. Statistical analysis
2. Programming (Python/R)
3. Data visualization
4. [continue the list]"
```

#### 🎯 Pattern Completion
```
"Example translations:
English: Hello → Spanish: Hola
English: Thank you → Spanish: Gracias
English: Goodbye → Spanish: [complete the pattern]"
```

### Advanced Completion Techniques

#### 🧩 Template Completion
```
"Product Review Template:
Product: [Product Name]
Rating: [1-5 stars]
Pros: [List advantages]
Cons: [List disadvantages]
Best for: [Target user]
Price: [Price range]

Now complete this template for the iPhone 15:"
```

#### 🔗 Chain Completion
```
"Complete this logical chain:
If global temperatures rise → Ice caps melt → Sea levels rise → Coastal cities flood → [what happens next?]"
```

### Best Practices
- Provide enough context for meaningful completion
- Use clear patterns when seeking pattern-based completion
- Specify the desired length or scope of completion
- Include examples when the pattern isn't obvious

## 💬 Conversational Prompts

Dialogue-based interactions that simulate natural conversation.

### Conversation Starters

#### 🎭 Role-based Conversations
```
"You are a career counselor. I'm a software engineer considering a career change to data science. Let's discuss my options."
```

#### 🤝 Collaborative Discussions
```
"Let's brainstorm innovative solutions for reducing plastic waste in restaurants. I'll share ideas, and you can build on them or suggest alternatives."
```

#### 🎓 Educational Dialogues
```
"I'm learning about machine learning. Can you explain gradient descent as if we're having a casual conversation? Feel free to ask me questions to check my understanding."
```

### Conversation Techniques

#### 📚 Socratic Method
```
"Instead of telling me about photosynthesis, help me discover it through questions. Ask me what I already know, then guide me to understand the process through inquiry."
```

#### 🎪 Debate Format
```
"Let's debate the pros and cons of remote work. You argue for remote work, I'll argue for in-office work. Start with your opening statement."
```

#### 🎯 Problem-Solving Dialogue
```
"I have a problem: my website loads slowly. Let's work through this together. Ask me diagnostic questions and help me identify solutions."
```

### Best Practices
- Establish clear roles and expectations
- Use natural, conversational language
- Encourage back-and-forth interaction
- Maintain context throughout the conversation

## 🎨 Creative Prompts

Prompts designed to generate artistic, imaginative, or original content.

### Creative Categories

#### ✍️ Creative Writing
```
"Write a short story about a librarian who discovers that books in their library are portals to other dimensions. Include:
- A compelling opening scene
- Character development
- A plot twist
- Vivid descriptions
- 800-1000 words"
```

#### 🎭 Character Creation
```
"Create a complex character for a cyberpunk novel:
- Name and background
- Personality traits and flaws
- Special skills or abilities
- Personal motivation and goals
- Relationships and conflicts
- Distinctive appearance or mannerisms"
```

#### 🌍 World Building
```
"Design a fantasy world where magic is powered by emotions:
- How does the magic system work?
- What are the societal implications?
- What conflicts arise from this system?
- Describe the political structure
- Create cultural traditions around emotion-magic"
```

#### 💡 Ideation Prompts
```
"Generate 10 innovative business ideas that combine:
- Sustainable practices
- Technology solutions
- Social impact
- Market viability

For each idea, include the problem it solves and potential target market."
```

### Creative Techniques

#### 🎲 Random Element Integration
```
"Write a story that must include these random elements:
- A purple umbrella
- A mathematician
- A haunted grocery store
- A secret code
- A talking cat

Weave these elements into a coherent narrative."
```

#### 🔄 Perspective Shifts
```
"Tell the story of Romeo and Juliet from the perspective of:
1. The balcony (as a sentient observer)
2. A modern-day social media influencer
3. A detective investigating the deaths
4. The families' pets"
```

### Best Practices
- Provide creative constraints to spark innovation
- Use vivid, descriptive language in prompts
- Encourage originality and unique perspectives
- Specify the desired creative medium or format

## 🧠 Analytical Prompts

Prompts that require analysis, reasoning, and critical thinking.

### Analysis Types

#### 📊 Data Analysis
```
"Analyze the following sales data trends:
Q1: $100K, Q2: $150K, Q3: $120K, Q4: $180K

Provide:
- Trend analysis
- Seasonal pattern identification
- Potential explanations for variations
- Predictions for next year
- Recommended actions"
```

#### 🔍 SWOT Analysis
```
"Conduct a SWOT analysis for a startup planning to launch a meal delivery service for seniors:

Strengths: [internal positive factors]
Weaknesses: [internal negative factors]
Opportunities: [external positive factors]
Threats: [external negative factors]

Include specific examples and strategic recommendations."
```

#### 🎯 Root Cause Analysis
```
"A software application crashes frequently. Perform a root cause analysis:

1. Identify potential causes (technical, environmental, user-related)
2. Prioritize causes by likelihood and impact
3. Suggest investigation methods for each cause
4. Recommend solutions and preventive measures
5. Create a testing plan to verify fixes"
```

#### 📈 Comparative Analysis
```
"Compare electric vehicles vs. hybrid vehicles across these dimensions:
- Environmental impact
- Cost of ownership
- Performance characteristics
- Infrastructure requirements
- Consumer adoption barriers

Provide a detailed comparison table and recommendation for different user profiles."
```

### Advanced Analytical Techniques

#### 🧩 Systems Thinking
```
"Analyze the education system as a complex system:
- Identify key components and stakeholders
- Map relationships and dependencies
- Identify feedback loops
- Analyze emergent properties
- Suggest system-level interventions"
```

#### 🎭 Scenario Analysis
```
"Analyze three scenarios for the future of remote work:

Scenario 1: Full return to office (80% in-office)
Scenario 2: Hybrid model (50/50 split)
Scenario 3: Fully remote (90% remote)

For each scenario, analyze:
- Business implications
- Employee satisfaction
- Productivity impacts
- Real estate effects
- Technology requirements"
```

### Best Practices
- Provide clear analytical frameworks
- Request specific outputs (tables, charts, recommendations)
- Include relevant data or context
- Specify the depth and scope of analysis

## 🎯 Few-Shot Learning Prompts

Prompts that include examples to guide the model's understanding.

### Zero-Shot vs. Few-Shot

#### Zero-Shot Example
```
"Translate the following sentence to French: 'The weather is beautiful today.'"
```

#### One-Shot Example
```
"Translate English to French:
English: Hello, how are you?
French: Bonjour, comment allez-vous?

English: The weather is beautiful today.
French:"
```

#### Few-Shot Example
```
"Translate English to French:
English: Hello, how are you?
French: Bonjour, comment allez-vous?

English: Thank you very much.
French: Merci beaucoup.

English: Where is the library?
French: Où est la bibliothèque?

English: The weather is beautiful today.
French:"
```

### Few-Shot Applications

#### 📧 Email Classification
```
"Classify emails by urgency:

Email: 'Meeting moved to tomorrow at 2 PM'
Urgency: Medium

Email: 'Server is down, customers can't access website'
Urgency: High

Email: 'Monthly newsletter with company updates'
Urgency: Low

Email: 'Client complaint about product defect'
Urgency:"
```

#### 🎯 Sentiment Analysis
```
"Analyze sentiment:

Review: 'This product exceeded my expectations!'
Sentiment: Positive

Review: 'Terrible quality, broke after one day'
Sentiment: Negative

Review: 'It's okay, nothing special'
Sentiment: Neutral

Review: 'Amazing customer service and fast delivery'
Sentiment:"
```

#### 💼 Business Classification
```
"Classify business ideas by industry:

Idea: 'AI-powered fitness coaching app'
Industry: Health & Technology

Idea: 'Sustainable packaging for restaurants'
Industry: Food & Environment

Idea: 'Virtual reality education platform'
Industry: Education & Technology

Idea: 'Peer-to-peer solar energy trading'
Industry:"
```

### Best Practices
- Choose representative examples
- Maintain consistent format across examples
- Include edge cases when relevant
- Ensure examples demonstrate the desired pattern clearly

## 🔗 Chain-of-Thought Prompts

Prompts that encourage step-by-step reasoning.

### Basic Chain-of-Thought

#### 🧮 Mathematical Reasoning
```
"Solve this step by step:

Problem: A store offers a 20% discount on all items. If a shirt originally costs $50, and there's an additional 10% tax on the final price, what's the total amount paid?

Step 1: Calculate the discount amount
Step 2: Find the discounted price
Step 3: Calculate the tax amount
Step 4: Find the final total

Show your work for each step."
```

#### 🤔 Logical Reasoning
```
"Think through this problem step by step:

All roses are flowers.
Some flowers are red.
All red things are beautiful.

Question: Are all roses beautiful?

Step 1: Identify what we know about roses
Step 2: Determine what we can conclude about roses being red
Step 3: Apply the rule about red things being beautiful
Step 4: Reach a conclusion"
```

### Advanced Chain-of-Thought

#### 🎯 Complex Problem Solving
```
"Let's solve this business problem step by step:

Problem: A SaaS company has 1000 users, 10% churn rate monthly, and wants to grow to 2000 users in 6 months.

Step 1: Calculate current monthly churn (users lost)
Step 2: Determine net growth needed per month
Step 3: Calculate required new user acquisition per month
Step 4: Assess if this growth rate is realistic
Step 5: Recommend strategies to achieve the goal

Walk through each step with calculations and reasoning."
```

#### 🧪 Scientific Reasoning
```
"Explain why ice floats on water using step-by-step reasoning:

Step 1: Consider the molecular structure of ice vs. liquid water
Step 2: Analyze density differences
Step 3: Apply Archimedes' principle
Step 4: Explain the practical implications
Step 5: Connect to real-world examples

Provide detailed reasoning for each step."
```

### Best Practices
- Explicitly request step-by-step reasoning
- Number or label each step clearly
- Ask for explanations at each step
- Use when dealing with complex or multi-faceted problems

## 🎭 Role-Based Prompts

Prompts that assign specific roles or personas to the AI.

### Professional Roles

#### 👨‍💼 Business Consultant
```
"You are a senior business consultant with 15 years of experience in digital transformation. A traditional retail company wants to build an e-commerce platform. Provide strategic advice covering:
- Market analysis approach
- Technology stack recommendations
- Implementation timeline
- Budget considerations
- Risk mitigation strategies"
```

#### 👩‍🏫 Expert Teacher
```
"You are an experienced high school physics teacher known for making complex concepts understandable. Explain quantum mechanics to your students using:
- Simple analogies
- Real-world examples
- Interactive questions
- Visual descriptions
- Common misconceptions to avoid"
```

#### 🎯 Subject Matter Expert
```
"You are a cybersecurity expert specializing in small business protection. A local restaurant owner asks about securing their customer data. Provide practical advice on:
- Essential security measures
- Budget-friendly solutions
- Staff training requirements
- Compliance considerations
- Incident response planning"
```

### Creative Roles

#### ✍️ Creative Writer
```
"You are a bestselling mystery novelist. Write the opening chapter of a murder mystery set in a small town library. Include:
- Atmospheric setting description
- Character introduction
- Subtle clues
- Engaging dialogue
- A compelling hook ending"
```

#### 🎨 Design Consultant
```
"You are a UX designer specializing in mobile apps. Critique this app concept and provide improvement recommendations:

App: Meditation app for busy professionals
Current features: 5-minute guided sessions, progress tracking, daily reminders

Provide feedback on:
- User experience flow
- Feature additions
- Interface design principles
- Accessibility considerations
- Competitive differentiation"
```

### Personality-Based Roles

#### 🎪 Enthusiastic Motivator
```
"You are an enthusiastic fitness coach who always finds the positive in every situation. Help someone who's struggling to maintain their exercise routine. Use your characteristic optimism and practical experience to:
- Acknowledge their struggles
- Reframe challenges as opportunities
- Provide actionable solutions
- Offer encouragement and motivation
- Create a sustainable plan"
```

#### 🤔 Analytical Thinker
```
"You are a methodical analyst who approaches problems with structured thinking. Analyze why a productivity app failed in the market:
- Systematic problem identification
- Data-driven hypothesis formation
- Logical cause-and-effect analysis
- Evidence-based conclusions
- Structured recommendations"
```

### Best Practices
- Choose roles that match the task requirements
- Provide background context for the role
- Specify expertise level and experience
- Include personality traits when relevant
- Maintain role consistency throughout the interaction

## 🎯 Contextual Prompts

Prompts that provide rich context to guide responses.

### Context Types

#### 🏢 Situational Context
```
"Context: You're presenting to the board of directors of a Fortune 500 company. The company is considering a $50M investment in AI technology. The board includes both tech-savvy and traditional business leaders.

Task: Explain the ROI potential of AI investment in terms that resonate with both audiences. Include specific examples, risk analysis, and implementation timeline."
```

#### 📊 Data Context
```
"Context: Here's our website analytics data:
- 100,000 monthly visitors
- 2% conversion rate
- Average order value: $85
- Bounce rate: 65%
- Mobile traffic: 70%

Task: Identify the top 3 optimization opportunities and provide specific, actionable recommendations for each."
```

#### 🎯 Audience Context
```
"Context: You're writing for senior citizens (ages 65-80) who are interested in technology but may lack technical expertise. They value clear explanations, practical benefits, and step-by-step guidance.

Task: Explain how to use video calling technology to stay connected with family, including setup, usage, and troubleshooting tips."
```

### Multi-Layered Context

#### 🌐 Comprehensive Context
```
"Context:
- Company: Tech startup, 50 employees, Series A funding
- Industry: Healthcare technology
- Challenge: Scaling customer support while maintaining quality
- Budget: $200K annually
- Timeline: 6 months to implement
- Stakeholders: CEO, CTO, Head of Customer Success
- Current situation: 2 support agents, 500+ monthly tickets, 24-hour response time

Task: Develop a comprehensive customer support scaling strategy including technology solutions, staffing recommendations, and process improvements."
```

## 🚀 Advanced Prompt Combinations

### Hybrid Approaches

#### 🎯 Instructional + Few-Shot + Chain-of-Thought
```
"You are a data analyst. Analyze customer feedback using this approach:

Example 1:
Feedback: "Love the product but shipping is slow"
Analysis: Product satisfaction (positive) + Logistics concern (negative)
Priority: Medium - improve shipping process
Action: Investigate shipping partners

Example 2:
Feedback: "Great customer service, solved my problem quickly"
Analysis: Service satisfaction (positive) + Efficiency (positive)
Priority: Low - maintain current standards
Action: Recognize service team

Now analyze this feedback step by step:
Feedback: "Product quality is poor, and the website is confusing"

Step 1: Identify sentiment components
Step 2: Categorize feedback types
Step 3: Assign priority level
Step 4: Recommend specific actions"
```

#### 🎭 Role + Analytical + Creative
```
"You are a marketing strategist for a sustainable fashion brand. 

Analyze our competitor landscape and create an innovative marketing campaign:

1. Competitive Analysis:
   - Identify 3 main competitors
   - Analyze their positioning
   - Find market gaps

2. Creative Campaign Development:
   - Develop unique value proposition
   - Create campaign concept
   - Design content strategy
   - Plan distribution channels

3. Success Metrics:
   - Define KPIs
   - Set realistic targets
   - Create measurement plan

Present your analysis and campaign as a professional marketing brief."
```

## 📊 Choosing the Right Prompt Type

### Decision Framework

#### 🎯 Task-Based Selection
- **Information Gathering**: Interrogative prompts
- **Content Creation**: Instructional + Creative prompts
- **Problem Solving**: Analytical + Chain-of-thought prompts
- **Learning/Teaching**: Conversational + Few-shot prompts
- **Decision Making**: Analytical + Role-based prompts

#### 🎪 Complexity-Based Selection
- **Simple Tasks**: Zero-shot instructional prompts
- **Medium Complexity**: Few-shot or contextual prompts
- **Complex Tasks**: Hybrid approaches with multiple techniques
- **Expert-Level Tasks**: Role-based + Chain-of-thought + Contextual

#### 🚀 Outcome-Based Selection
- **Factual Information**: Interrogative prompts
- **Creative Content**: Creative + Role-based prompts
- **Analysis/Insights**: Analytical + Chain-of-thought prompts
- **Practical Solutions**: Instructional + Contextual prompts
- **Learning Materials**: Conversational + Few-shot prompts

## 🎓 Key Takeaways

### Essential Principles
1. **Match prompt type to task requirements**
2. **Combine techniques for complex tasks**
3. **Provide appropriate context and examples**
4. **Consider your audience and output format**
5. **Iterate and refine based on results**

### Quick Reference Guide
- **Need facts?** → Interrogative prompts
- **Want creativity?** → Creative + Role-based prompts
- **Require analysis?** → Analytical + Chain-of-thought prompts
- **Teaching concept?** → Few-shot + Conversational prompts
- **Solving problems?** → Contextual + Instructional prompts

### Next Steps
1. Practice with different prompt types
2. Experiment with combinations
3. Develop templates for common tasks
4. Study successful prompts in your domain
5. Build a personal prompt library

---

**Ready to master prompt refinement?** Continue with [Refining and Iterating](04_refining_and_iterating.md) to learn how to improve any prompt systematically.

**Remember:** The best prompt type depends on your specific task, audience, and desired outcome. Don't be afraid to experiment and combine different approaches!
