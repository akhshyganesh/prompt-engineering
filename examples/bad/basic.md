# ❌ Bad Basic Prompt Examples

This file contains examples of poorly crafted prompts and explains why they fail, along with improved versions.

## 🚫 Common Prompt Failures

### ❌ Too Vague and Generic

#### Example 1: Content Creation
**Bad Prompt:**
```
Write about AI.
```

**Problems:**
- ❌ No specific topic focus
- ❌ No target audience
- ❌ No length specification
- ❌ No format or structure
- ❌ No tone or style guidance

**Improved Version:**
```
Write a 500-word blog post explaining how AI is transforming healthcare for patients and doctors. Include specific examples of AI applications (diagnosis, treatment, administration) and address common concerns about AI replacing human care. Target audience: general public with basic health awareness. Use an informative but reassuring tone.
```

#### Example 2: Business Communication
**Bad Prompt:**
```
Write an email.
```

**Problems:**
- ❌ No recipient specified
- ❌ No purpose stated
- ❌ No context provided
- ❌ No tone guidance
- ❌ No call-to-action

**Improved Version:**
```
Write a professional email to a potential client who requested information about our web development services. Include our key service offerings, mention our 10+ years of experience, provide 2-3 client success examples, and invite them to schedule a consultation call. Keep it concise (under 200 words) and use a friendly but professional tone.
```

### ❌ Ambiguous Instructions

#### Example 3: Analysis Task
**Bad Prompt:**
```
Analyze this data.
```

**Problems:**
- ❌ No data provided
- ❌ No analysis type specified
- ❌ No deliverable format
- ❌ No analytical framework
- ❌ No audience consideration

**Improved Version:**
```
Analyze the quarterly sales data I'm providing below. Focus on:
- Revenue trends across Q1-Q4
- Top performing product categories
- Regional performance comparison
- Seasonal patterns identification
Create a summary report with key insights and 3 actionable recommendations for Q1 next year. Format as executive summary for board presentation.

[Sales Data]
Q1: $500K, Q2: $750K, Q3: $600K, Q4: $900K
Product A: 40%, Product B: 35%, Product C: 25%
Regions: North (45%), South (30%), West (25%)
```

#### Example 4: Creative Task
**Bad Prompt:**
```
Be creative.
```

**Problems:**
- ❌ No creative medium specified
- ❌ No subject or theme
- ❌ No constraints or parameters
- ❌ No success criteria
- ❌ Completely open-ended

**Improved Version:**
```
Create 5 creative marketing slogans for an eco-friendly cleaning product company. Each slogan should:
- Be under 8 words
- Emphasize environmental benefits
- Include wordplay or alliteration if possible
- Appeal to environmentally conscious families
- Be memorable and easy to say
Examples of tone: friendly, trustworthy, inspiring
```

### ❌ Missing Context

#### Example 5: Technical Explanation
**Bad Prompt:**
```
Explain blockchain.
```

**Problems:**
- ❌ No audience specified
- ❌ No depth level indicated
- ❌ No application context
- ❌ No length constraints
- ❌ No format preference

**Improved Version:**
```
Explain blockchain technology to small business owners who are considering accepting cryptocurrency payments. Focus on:
- Basic concept in simple terms (avoid technical jargon)
- How it ensures security and trust
- Practical implications for their business
- Common concerns and misconceptions
Keep explanation under 300 words and use analogies to familiar concepts like bank ledgers or public records.
```

#### Example 6: Problem Solving
**Bad Prompt:**
```
Fix this problem.
```

**Problems:**
- ❌ No problem description
- ❌ No context provided
- ❌ No constraints specified
- ❌ No solution format
- ❌ No evaluation criteria

**Improved Version:**
```
Help solve this customer service problem: Our online store receives 100+ support tickets daily, but we only have 2 agents responding within 48 hours, causing customer frustration.

Current situation:
- 2 full-time support agents
- Average response time: 48 hours
- Customer satisfaction: 60%
- Budget: $5K monthly for improvements

Provide 3 specific solutions with:
- Implementation steps
- Expected impact on response time
- Cost implications
- Timeline for results
```

### ❌ Overwhelming Complexity

#### Example 7: Multiple Conflicting Requests
**Bad Prompt:**
```
Write a comprehensive guide about everything related to digital marketing including SEO, social media, email marketing, content marketing, PPC advertising, analytics, conversion optimization, influencer marketing, video marketing, and mobile marketing with examples, case studies, tools, strategies, best practices, common mistakes, future trends, budget considerations, and ROI calculations for beginners, intermediate, and advanced users in both B2B and B2C contexts across different industries while keeping it concise and actionable.
```

**Problems:**
- ❌ Too many topics at once
- ❌ Contradictory requirements (comprehensive vs. concise)
- ❌ Multiple audiences specified
- ❌ Unrealistic scope
- ❌ Information overload

**Improved Version:**
```
Write a beginner's guide to digital marketing for small business owners. Focus on the 3 most important channels for local businesses:
1. Search Engine Optimization (SEO) basics
2. Social media marketing fundamentals  
3. Email marketing essentials

For each channel, include:
- What it is and why it matters
- 3-5 actionable first steps
- One simple success metric to track
- Common beginner mistakes to avoid

Target length: 1500 words total (500 per channel)
Tone: practical, encouraging, jargon-free
```

### ❌ Assumed Knowledge

#### Example 8: Technical Instructions
**Bad Prompt:**
```
Implement the API.
```

**Problems:**
- ❌ Which API not specified
- ❌ Programming language unclear
- ❌ No context about the project
- ❌ No success criteria
- ❌ Assumes prior knowledge

**Improved Version:**
```
Help me implement a REST API integration for user authentication in my Python Flask application. I need to:
- Connect to Auth0 for user login/logout
- Store user session data
- Protect specific routes that require authentication
- Handle login errors gracefully

My experience level: Intermediate Python, new to API integrations
Provide step-by-step code examples with explanations for each step.
```

#### Example 9: Domain-Specific Jargon
**Bad Prompt:**
```
Optimize the conversion funnel using A/B testing methodologies.
```

**Problems:**
- ❌ Assumes marketing expertise
- ❌ No business context
- ❌ No specific goals
- ❌ Technical jargon without explanation
- ❌ No implementation details

**Improved Version:**
```
I run an e-commerce website selling handmade jewelry. Currently, 1000 people visit my product pages monthly, but only 20 make purchases (2% conversion rate). 

Help me improve this by:
- Identifying 3 key areas where visitors might be dropping off
- Suggesting specific A/B test ideas for each area
- Explaining how to measure success
- Providing implementation steps for someone with basic website management skills

Goal: Increase conversion rate to 4% within 3 months
```

### ❌ No Success Criteria

#### Example 10: Subjective Tasks
**Bad Prompt:**
```
Make this better.
```

**Problems:**
- ❌ No baseline provided
- ❌ "Better" not defined
- ❌ No specific improvements requested
- ❌ No evaluation criteria
- ❌ Completely subjective

**Improved Version:**
```
Improve this product description for better conversion:

[Current Description]
"Our headphones are good quality and affordable. Many people like them. They work well for music."

Improvements needed:
- Add specific technical features
- Include emotional benefits
- Use persuasive language
- Add social proof elements
- Optimize for online shoppers
- Target audience: music enthusiasts, budget-conscious

Goal: Increase click-through rate and reduce bounce rate
Length: 2-3 paragraphs maximum
```

## 🎯 Pattern Recognition: Why Prompts Fail

### The "Mind Reader" Problem
Bad prompts expect AI to read your mind:
```
❌ "Help me with my project"
✅ "Help me create a project timeline for launching a mobile app in 6 months"
```

### The "Everything Everywhere" Problem
Bad prompts try to do too much:
```
❌ "Write about technology and its impact on society, economics, education, healthcare, and the environment"
✅ "Write about technology's impact on remote work, focusing on productivity tools and work-life balance"
```

### The "Assumption" Problem
Bad prompts assume knowledge or context:
```
❌ "Fix the bug in line 42"
✅ "Fix this Python error: 'list index out of range' in line 42 of my data processing script: [provide code]"
```

### The "Vague Outcome" Problem
Bad prompts don't specify what success looks like:
```
❌ "Make this presentation better"
✅ "Improve this presentation's clarity for a 15-minute board meeting, focusing on key metrics and actionable recommendations"
```

## 🔧 Quick Improvement Checklist

Before submitting any prompt, check:

### ✅ The Specificity Test
- [ ] Is the task clearly defined?
- [ ] Are requirements specific?
- [ ] Is the scope appropriate?

### ✅ The Context Test
- [ ] Is background information provided?
- [ ] Is the audience specified?
- [ ] Are constraints mentioned?

### ✅ The Clarity Test
- [ ] Would a human understand this clearly?
- [ ] Are there any ambiguous terms?
- [ ] Is the language appropriate for the task?

### ✅ The Completeness Test
- [ ] Are all necessary details included?
- [ ] Is the desired output format specified?
- [ ] Are success criteria defined?

### ✅ The Realistic Test
- [ ] Is the request feasible?
- [ ] Are expectations reasonable?
- [ ] Is the scope manageable?

## 🚀 Transform Bad Prompts Exercise

### Practice Set 1: Fix These Prompts

**Bad Prompt 1:** "Tell me about marketing"
**Your Improved Version:** ________________

**Bad Prompt 2:** "Write code"
**Your Improved Version:** ________________

**Bad Prompt 3:** "Analyze this situation"
**Your Improved Version:** ________________

### Practice Set 2: Identify Problems

For each prompt, identify what's wrong:

**Prompt A:** "Create something innovative for my business"
**Problems:** ________________

**Prompt B:** "Explain quantum computing, machine learning, blockchain, and cybersecurity"
**Problems:** ________________

**Prompt C:** "Write a good email"
**Problems:** ________________

## 🎓 Key Learning Points

### Red Flags to Avoid
- Starting with vague words: "something," "anything," "stuff"
- Using undefined terms: "better," "good," "professional"
- Multiple conflicting requirements
- No context or background
- Assuming prior knowledge

### Green Flags to Include
- Specific, measurable requirements
- Clear audience and context
- Defined success criteria
- Appropriate scope and constraints
- Actionable outcomes

### The Golden Rule
**If you wouldn't understand your own prompt without additional explanation, neither will the AI.**

## 🔄 Before and After Summary

| Bad Prompt Characteristics | Good Prompt Characteristics |
|----------------------------|----------------------------|
| Vague and generic | Specific and detailed |
| No context provided | Rich context included |
| Ambiguous instructions | Clear, actionable steps |
| Overwhelming scope | Focused, manageable scope |
| No success criteria | Defined outcomes |
| Assumes knowledge | Provides necessary background |
| No audience specified | Clear target audience |
| No format preference | Specific format requirements |

**Remember:** Every bad prompt is a learning opportunity. The goal isn't perfection on the first try, but continuous improvement through iteration and learning from what doesn't work.

**Next Step:** Study the [Good Basic Examples](../good/basic.md) to see these principles applied correctly.
