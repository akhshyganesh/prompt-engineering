#!/usr/bin/env python3
"""
Basic Prompt Engineering Examples

This script demonstrates fundamental prompt engineering techniques using Python.
It shows how to structure prompts, handle responses, and implement best practices.
"""

import os
import json
import time
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from enum import Enum

import openai
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class PromptType(Enum):
    """Enumeration of different prompt types."""
    INSTRUCTIONAL = "instructional"
    INTERROGATIVE = "interrogative" 
    COMPLETION = "completion"
    CREATIVE = "creative"
    ANALYTICAL = "analytical"
    CONVERSATIONAL = "conversational"

@dataclass
class PromptConfig:
    """Configuration for prompt execution."""
    model: str = "gpt-3.5-turbo"
    temperature: float = 0.7
    max_tokens: int = 1000
    top_p: float = 1.0
    frequency_penalty: float = 0.0
    presence_penalty: float = 0.0

@dataclass
class PromptResult:
    """Result container for prompt execution."""
    prompt: str
    response: str
    prompt_type: PromptType
    tokens_used: int
    execution_time: float
    cost_estimate: float

class BasicPromptEngineer:
    """
    A basic prompt engineering class demonstrating fundamental techniques.
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the prompt engineer with OpenAI client."""
        self.client = OpenAI(api_key=api_key or os.getenv("OPENAI_API_KEY"))
        self.config = PromptConfig()
        self.results_history: List[PromptResult] = []
    
    def execute_prompt(self, 
                      prompt: str, 
                      prompt_type: PromptType = PromptType.INSTRUCTIONAL,
                      config: Optional[PromptConfig] = None) -> PromptResult:
        """
        Execute a prompt and return structured results.
        
        Args:
            prompt: The prompt text to execute
            prompt_type: Type of prompt being executed
            config: Optional configuration override
            
        Returns:
            PromptResult containing response and metadata
        """
        
        # Use provided config or default
        exec_config = config or self.config
        
        # Record start time
        start_time = time.time()
        
        try:
            # Execute the prompt
            response = self.client.chat.completions.create(
                model=exec_config.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=exec_config.temperature,
                max_tokens=exec_config.max_tokens,
                top_p=exec_config.top_p,
                frequency_penalty=exec_config.frequency_penalty,
                presence_penalty=exec_config.presence_penalty
            )
            
            # Calculate execution time
            execution_time = time.time() - start_time
            
            # Extract response content
            response_text = response.choices[0].message.content
            
            # Calculate token usage
            tokens_used = response.usage.total_tokens
            
            # Estimate cost (approximate)
            cost_estimate = self._estimate_cost(tokens_used, exec_config.model)
            
            # Create result object
            result = PromptResult(
                prompt=prompt,
                response=response_text,
                prompt_type=prompt_type,
                tokens_used=tokens_used,
                execution_time=execution_time,
                cost_estimate=cost_estimate
            )
            
            # Store in history
            self.results_history.append(result)
            
            return result
            
        except Exception as e:
            print(f"Error executing prompt: {str(e)}")
            raise
    
    def _estimate_cost(self, tokens: int, model: str) -> float:
        """Estimate cost based on token usage and model."""
        # Approximate costs per 1K tokens (as of 2024)
        cost_per_1k = {
            "gpt-4": 0.03,
            "gpt-4-turbo": 0.01,
            "gpt-3.5-turbo": 0.002,
            "gpt-3.5-turbo-16k": 0.004
        }
        
        rate = cost_per_1k.get(model, 0.002)  # Default to GPT-3.5 rate
        return (tokens / 1000) * rate
    
    def demonstrate_instructional_prompts(self):
        """Demonstrate various instructional prompt techniques."""
        
        print("🎯 INSTRUCTIONAL PROMPTS DEMO")
        print("=" * 50)
        
        # Example 1: Basic instruction
        print("\n1. Basic Instruction Example:")
        basic_prompt = """
        Write a professional email to thank a client for their business.
        Include appreciation for their trust and mention looking forward to future collaboration.
        Keep it concise and warm in tone.
        """
        
        result = self.execute_prompt(basic_prompt.strip(), PromptType.INSTRUCTIONAL)
        print(f"Prompt: {result.prompt}")
        print(f"Response: {result.response}")
        print(f"Tokens: {result.tokens_used}, Time: {result.execution_time:.2f}s")
        
        # Example 2: Detailed instruction with constraints
        print("\n2. Detailed Instruction with Constraints:")  
        detailed_prompt = """
        Create a social media post about sustainable living tips.
        
        Requirements:
        - Target audience: Young professionals aged 25-35
        - Platform: LinkedIn 
        - Length: 200-250 words
        - Tone: Professional yet approachable
        - Include 3 specific actionable tips
        - End with a question to encourage engagement
        - Use relevant hashtags (3-5 hashtags)
        """
        
        result = self.execute_prompt(detailed_prompt.strip(), PromptType.INSTRUCTIONAL)
        print(f"Response: {result.response}")
        
        # Example 3: Step-by-step instruction
        print("\n3. Step-by-Step Instruction:")
        step_prompt = """
        Explain how to change a car tire in a step-by-step format.
        
        Structure your response as:
        1. Safety preparations (2-3 steps)
        2. Removing the flat tire (4-5 steps)  
        3. Installing the spare tire (3-4 steps)
        4. Final safety checks (2-3 steps)
        
        Use clear, simple language suitable for someone who has never changed a tire.
        Include safety warnings where appropriate.
        """
        
        result = self.execute_prompt(step_prompt.strip(), PromptType.INSTRUCTIONAL)
        print(f"Response: {result.response}")
    
    def demonstrate_interrogative_prompts(self):
        """Demonstrate interrogative (question-based) prompts."""
        
        print("\n❓ INTERROGATIVE PROMPTS DEMO")
        print("=" * 50)
        
        # Example 1: Open-ended question
        print("\n1. Open-ended Question:")
        open_question = """
        What are the most significant challenges facing remote teams in 2024, 
        and how can organizations address these challenges effectively?
        
        Please structure your answer with:
        - 3 main challenges
        - Specific solutions for each challenge
        - Implementation timeline considerations
        """
        
        result = self.execute_prompt(open_question.strip(), PromptType.INTERROGATIVE)
        print(f"Response: {result.response}")
        
        # Example 2: Comparative question
        print("\n2. Comparative Question:")
        comparative_question = """
        Compare Python and JavaScript for web development from these perspectives:
        
        1. Learning curve for beginners
        2. Performance characteristics  
        3. Ecosystem and library support
        4. Job market opportunities
        5. Long-term career prospects
        
        Provide a balanced analysis with specific examples and recommendations 
        for different developer profiles.
        """
        
        result = self.execute_prompt(comparative_question.strip(), PromptType.INTERROGATIVE)
        print(f"Response: {result.response}")
        
        # Example 3: Analytical question
        print("\n3. Analytical Question:")
        analytical_question = """
        Why do many startups fail within their first two years, and what patterns 
        can be identified from successful startups that survived this critical period?
        
        Analyze:
        - Top 5 failure reasons with statistics
        - Success patterns from unicorn companies
        - Actionable advice for early-stage founders
        - Industry-specific considerations
        """
        
        result = self.execute_prompt(analytical_question.strip(), PromptType.INTERROGATIVE)
        print(f"Response: {result.response}")
    
    def demonstrate_few_shot_learning(self):
        """Demonstrate few-shot learning techniques."""
        
        print("\n🎯 FEW-SHOT LEARNING DEMO")
        print("=" * 50)
        
        # Example 1: Email classification
        print("\n1. Email Classification with Examples:")
        few_shot_classification = """
        Classify the following emails by urgency level (High, Medium, Low):
        
        Examples:
        Email: "Server is down, customers cannot access our website"
        Urgency: High
        
        Email: "Quarterly team meeting scheduled for next Friday"  
        Urgency: Medium
        
        Email: "Monthly newsletter with company updates"
        Urgency: Low
        
        Email: "Client complaining about product defect affecting their production"
        Urgency: High
        
        Now classify:
        Email: "Request for proposal deadline is tomorrow, need final review"
        Urgency:
        """
        
        result = self.execute_prompt(few_shot_classification.strip(), PromptType.ANALYTICAL)
        print(f"Response: {result.response}")
        
        # Example 2: Product description generation
        print("\n2. Product Description Pattern Learning:")
        product_description_pattern = """
        Generate product descriptions following this pattern:
        
        Example 1:
        Product: Wireless Bluetooth Headphones
        Description: Experience crystal-clear audio with our premium wireless Bluetooth headphones. 
        Featuring 30-hour battery life, noise-cancellation technology, and ergonomic design for 
        all-day comfort. Perfect for music lovers, podcast enthusiasts, and professionals on-the-go.
        
        Example 2:
        Product: Stainless Steel Water Bottle
        Description: Stay hydrated in style with our double-wall insulated water bottle. Keeps 
        drinks cold for 24 hours or hot for 12 hours. Made from premium stainless steel with 
        leak-proof design. Ideal for fitness enthusiasts, office workers, and outdoor adventurers.
        
        Now generate for:
        Product: Smart Home Security Camera
        Description:
        """
        
        result = self.execute_prompt(product_description_pattern.strip(), PromptType.CREATIVE)
        print(f"Response: {result.response}")
    
    def demonstrate_chain_of_thought(self):
        """Demonstrate chain-of-thought reasoning."""
        
        print("\n🧠 CHAIN-OF-THOUGHT REASONING DEMO") 
        print("=" * 50)
        
        # Example 1: Problem-solving with steps
        print("\n1. Step-by-Step Problem Solving:")
        cot_problem = """
        Let's solve this business problem step by step:
        
        Problem: A SaaS company has 1,000 active users paying $50/month. They want to 
        double their revenue in 12 months. Current churn rate is 5% monthly.
        
        Think through this step by step:
        
        Step 1: Calculate current monthly revenue
        Step 2: Determine target revenue in 12 months  
        Step 3: Calculate net user growth needed (accounting for churn)
        Step 4: Identify strategies to achieve this growth
        Step 5: Assess feasibility and recommend action plan
        
        Work through each step with calculations and reasoning.
        """
        
        result = self.execute_prompt(cot_problem.strip(), PromptType.ANALYTICAL)
        print(f"Response: {result.response}")
        
        # Example 2: Technical decision making
        print("\n2. Technical Decision Chain of Thought:")
        tech_decision = """
        Help me choose between microservices and monolith architecture for a new project.
        Walk through the decision-making process:
        
        Step 1: Analyze project requirements
        - Team size: 8 developers
        - Expected user base: 100K users in first year
        - Feature complexity: Medium (e-commerce platform)
        - Timeline: 6 months to market
        
        Step 2: Compare architectural approaches
        - Development speed and complexity
        - Scalability requirements
        - Team expertise and resources
        - Maintenance and operational overhead
        
        Step 3: Evaluate trade-offs
        - Short-term vs long-term considerations
        - Risk assessment
        - Migration possibilities
        
        Step 4: Make recommendation with justification
        
        Think through each step systematically.
        """
        
        result = self.execute_prompt(tech_decision.strip(), PromptType.ANALYTICAL)
        print(f"Response: {result.response}")
    
    def demonstrate_role_based_prompts(self):
        """Demonstrate role-based prompting techniques."""
        
        print("\n🎭 ROLE-BASED PROMPTS DEMO")
        print("=" * 50)
        
        # Example 1: Expert consultant role
        print("\n1. Expert Consultant Role:")
        consultant_role = """
        You are a senior digital marketing consultant with 15 years of experience 
        helping small businesses grow their online presence. You're known for providing 
        practical, actionable advice that delivers measurable results.
        
        A local restaurant owner approaches you. They have:
        - 50 seats, family-owned for 20 years
        - Strong local reputation but minimal online presence
        - Budget of $2,000/month for digital marketing
        - Goal: Increase delivery orders by 40% in 6 months
        
        Provide a comprehensive digital marketing strategy including:
        - Priority channels and tactics
        - Budget allocation recommendations
        - Implementation timeline
        - Success metrics and KPIs
        - Common pitfalls to avoid
        
        Draw from your expertise to give specific, actionable advice.
        """
        
        result = self.execute_prompt(consultant_role.strip(), PromptType.ANALYTICAL)
        print(f"Response: {result.response}")
        
        # Example 2: Teacher role
        print("\n2. Expert Teacher Role:")
        teacher_role = """
        You are an experienced high school computer science teacher who excels at 
        making complex programming concepts accessible to beginners. You use analogies, 
        real-world examples, and interactive questions to help students understand.
        
        A student asks: "I don't understand what APIs are or why they're important. 
        Can you explain it in a way that makes sense?"
        
        As their teacher:
        - Use simple, relatable analogies
        - Provide concrete examples they can relate to
        - Ask questions to check understanding
        - Give them a practical next step to explore APIs
        - Maintain an encouraging, patient tone
        """
        
        result = self.execute_prompt(teacher_role.strip(), PromptType.CONVERSATIONAL)
        print(f"Response: {result.response}")
    
    def demonstrate_creative_prompts(self):
        """Demonstrate creative prompting techniques."""
        
        print("\n🎨 CREATIVE PROMPTS DEMO")
        print("=" * 50)
        
        # Example 1: Story creation with constraints
        print("\n1. Creative Story with Constraints:")
        creative_story = """
        Write a 400-word short story that includes these exact elements:
        - A mysterious package delivered to the wrong address
        - A character who collects vintage postcards  
        - A rainy Tuesday evening
        - A discovery that changes everything
        - The phrase "some secrets are worth keeping"
        
        Requirements:
        - Genre: Contemporary mystery
        - Tone: Intriguing but hopeful
        - Include dialogue
        - Create a satisfying resolution
        - Show don't tell - use vivid descriptions
        """
        
        result = self.execute_prompt(creative_story.strip(), PromptType.CREATIVE)
        print(f"Response: {result.response}")
        
        # Example 2: Creative problem solving
        print("\n2. Creative Business Brainstorming:")
        creative_business = """
        Generate 5 innovative business ideas that combine these elements:
        - Sustainability/environmental focus
        - Technology/digital solution
        - Social impact/community benefit
        - Profitable business model
        
        For each idea, provide:
        - Catchy business name
        - One-sentence description
        - Target market
        - Revenue model
        - Unique value proposition
        - Implementation difficulty (1-10 scale)
        
        Think outside the box - be creative but realistic!
        """
        
        result = self.execute_prompt(creative_business.strip(), PromptType.CREATIVE)
        print(f"Response: {result.response}")
    
    def demonstrate_optimization_techniques(self):
        """Demonstrate prompt optimization techniques."""
        
        print("\n⚡ PROMPT OPTIMIZATION DEMO")
        print("=" * 50)
        
        # Example 1: Before and after optimization
        print("\n1. Prompt Optimization Example:")
        
        # Original (weak) prompt
        weak_prompt = "Write about AI in healthcare."
        
        print("BEFORE (Weak Prompt):")
        print(f"'{weak_prompt}'")
        
        result_weak = self.execute_prompt(weak_prompt, PromptType.INSTRUCTIONAL)
        print(f"Response length: {len(result_weak.response)} characters")
        print(f"Tokens used: {result_weak.tokens_used}")
        
        # Optimized (strong) prompt
        strong_prompt = """
        Write a comprehensive analysis of AI applications in healthcare for hospital 
        administrators considering AI implementation.
        
        Structure:
        1. Executive Summary (2-3 sentences)
        2. Current AI Applications (3 specific examples with ROI data)
        3. Implementation Challenges (3 main obstacles with solutions)
        4. Future Opportunities (2-3 emerging trends)
        5. Action Steps (5 concrete next steps)
        
        Requirements:
        - Professional tone for C-level audience
        - Include specific statistics and examples
        - Address budget and resource considerations
        - Length: 800-1000 words
        - Actionable recommendations only
        """
        
        print("\nAFTER (Optimized Prompt):")
        print(f"'{strong_prompt.strip()[:100]}...'")
        
        result_strong = self.execute_prompt(strong_prompt.strip(), PromptType.ANALYTICAL)
        print(f"Response length: {len(result_strong.response)} characters")
        print(f"Tokens used: {result_strong.tokens_used}")
        
        print(f"\nImprovement: {((len(result_strong.response) / len(result_weak.response)) - 1) * 100:.1f}% more detailed response")
    
    def generate_performance_report(self):
        """Generate a performance report of all executed prompts."""
        
        if not self.results_history:
            print("No prompts executed yet.")
            return
        
        print("\n📊 PERFORMANCE REPORT")
        print("=" * 50)
        
        total_prompts = len(self.results_history)
        total_tokens = sum(r.tokens_used for r in self.results_history)
        total_cost = sum(r.cost_estimate for r in self.results_history)
        avg_execution_time = sum(r.execution_time for r in self.results_history) / total_prompts
        
        print(f"Total Prompts Executed: {total_prompts}")
        print(f"Total Tokens Used: {total_tokens:,}")
        print(f"Total Estimated Cost: ${total_cost:.4f}")
        print(f"Average Execution Time: {avg_execution_time:.2f} seconds")
        
        # Breakdown by prompt type
        type_breakdown = {}
        for result in self.results_history:
            ptype = result.prompt_type.value
            if ptype not in type_breakdown:
                type_breakdown[ptype] = {"count": 0, "tokens": 0, "cost": 0}
            type_breakdown[ptype]["count"] += 1
            type_breakdown[ptype]["tokens"] += result.tokens_used
            type_breakdown[ptype]["cost"] += result.cost_estimate
        
        print("\nBreakdown by Prompt Type:")
        for ptype, stats in type_breakdown.items():
            print(f"  {ptype.title()}: {stats['count']} prompts, {stats['tokens']} tokens, ${stats['cost']:.4f}")
    
    def save_results(self, filename: str = "prompt_results.json"):
        """Save all results to a JSON file."""
        
        results_data = []
        for result in self.results_history:
            results_data.append({
                "prompt": result.prompt,
                "response": result.response,
                "prompt_type": result.prompt_type.value,
                "tokens_used": result.tokens_used,
                "execution_time": result.execution_time,
                "cost_estimate": result.cost_estimate
            })
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(results_data, f, indent=2, ensure_ascii=False)
        
        print(f"Results saved to {filename}")


def main():
    """Main demonstration function."""
    
    print("🚀 BASIC PROMPT ENGINEERING DEMONSTRATION")
    print("=" * 60)
    
    # Initialize the prompt engineer
    try:
        engineer = BasicPromptEngineer()
        print("✅ OpenAI client initialized successfully")
    except Exception as e:
        print(f"❌ Failed to initialize OpenAI client: {e}")
        print("Please check your OPENAI_API_KEY environment variable.")
        return
    
    # Run demonstrations
    demonstrations = [
        ("Instructional Prompts", engineer.demonstrate_instructional_prompts),
        ("Interrogative Prompts", engineer.demonstrate_interrogative_prompts),
        ("Few-Shot Learning", engineer.demonstrate_few_shot_learning),
        ("Chain-of-Thought Reasoning", engineer.demonstrate_chain_of_thought),
        ("Role-Based Prompts", engineer.demonstrate_role_based_prompts),
        ("Creative Prompts", engineer.demonstrate_creative_prompts),
        ("Optimization Techniques", engineer.demonstrate_optimization_techniques)
    ]
    
    for demo_name, demo_func in demonstrations:
        try:
            print(f"\n🎯 Running {demo_name} demonstration...")
            demo_func()
            print(f"✅ {demo_name} completed successfully")
        except Exception as e:
            print(f"❌ Error in {demo_name}: {e}")
            continue
    
    # Generate final report
    engineer.generate_performance_report()
    
    # Save results
    engineer.save_results("basic_prompting_results.json")
    
    print("\n🎉 All demonstrations completed!")
    print("Check the generated JSON file for detailed results.")


if __name__ == "__main__":
    main()
