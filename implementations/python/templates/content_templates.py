"""
Content Template Engine for Prompt Engineering

This module provides templates for various content creation tasks including
blog posts, articles, social media content, and marketing materials.
"""

from typing import Dict, List, Optional, Any, Union
from dataclasses import dataclass
from enum import Enum
import json
import re

class ContentType(Enum):
    """Enumeration of content types."""
    BLOG_POST = "blog_post"
    ARTICLE = "article"
    SOCIAL_MEDIA = "social_media"
    EMAIL = "email"
    PRODUCT_DESCRIPTION = "product_description"
    PRESS_RELEASE = "press_release"
    NEWSLETTER = "newsletter"
    LANDING_PAGE = "landing_page"

class ToneType(Enum):
    """Enumeration of content tones."""
    PROFESSIONAL = "professional"
    CASUAL = "casual" 
    FRIENDLY = "friendly"
    AUTHORITATIVE = "authoritative"
    CONVERSATIONAL = "conversational"
    FORMAL = "formal"
    HUMOROUS = "humorous"
    INSPIRING = "inspiring"
    URGENT = "urgent"
    PERSUASIVE = "persuasive"

@dataclass
class ContentTemplate:
    """Template configuration for content generation."""
    content_type: ContentType
    template_name: str
    prompt_template: str
    required_params: List[str]
    optional_params: List[str]
    default_config: Dict[str, Any]
    examples: List[Dict[str, str]]

class ContentTemplateEngine:
    """Engine for generating content using prompt templates."""
    
    def __init__(self):
        """Initialize the content template engine."""
        self.templates: Dict[str, ContentTemplate] = {}
        self._load_default_templates()
    
    def _load_default_templates(self):
        """Load default content templates."""
        
        # Blog Post Template
        blog_post_template = ContentTemplate(
            content_type=ContentType.BLOG_POST,
            template_name="comprehensive_blog_post",
            prompt_template="""
            Write a comprehensive blog post about {topic} for {target_audience}.
            
            Article Requirements:
            - Length: {word_count} words
            - Tone: {tone}
            - Include: {key_points}
            - SEO Focus: {seo_keywords}
            
            Structure:
            1. Compelling headline that includes primary keyword
            2. Engaging introduction with hook
            3. {num_sections} main sections with subheadings
            4. Practical examples and actionable insights
            5. Conclusion with clear call-to-action
            
            Additional Instructions:
            - Use {tone} tone throughout
            - Include relevant statistics or data points
            - Add transition sentences between sections
            - Optimize for readability and SEO
            - End with engaging question for comments
            
            {additional_instructions}
            """.strip(),
            required_params=["topic", "target_audience", "word_count", "tone"],
            optional_params=["key_points", "seo_keywords", "num_sections", "additional_instructions"],
            default_config={
                "word_count": 1000,
                "tone": "professional",
                "num_sections": 3,
                "key_points": "main benefits and practical applications",
                "seo_keywords": "relevant industry keywords",
                "additional_instructions": ""
            },
            examples=[
                {
                    "topic": "Remote Work Productivity",
                    "target_audience": "working professionals",
                    "output_sample": "# Boost Your Remote Work Productivity: 7 Proven Strategies..."
                }
            ]
        )
        
        # Social Media Template
        social_media_template = ContentTemplate(
            content_type=ContentType.SOCIAL_MEDIA,
            template_name="engaging_social_post",
            prompt_template="""
            Create a {platform} post about {topic} for {target_audience}.
            
            Post Requirements:
            - Platform: {platform}
            - Character limit: {char_limit}
            - Tone: {tone}
            - Include: {content_elements}
            
            Elements to include:
            - Hook: Attention-grabbing opening line
            - Value: Clear benefit or insight
            - Engagement: Question or call-to-action
            - Hashtags: {num_hashtags} relevant hashtags
            - Emojis: Use appropriately for platform
            
            Platform-specific optimization:
            {platform_specific_instructions}
            
            Additional requirements:
            {additional_requirements}
            """.strip(),
            required_params=["platform", "topic", "target_audience"],
            optional_params=["char_limit", "tone", "content_elements", "num_hashtags", "platform_specific_instructions", "additional_requirements"],
            default_config={
                "char_limit": 280,
                "tone": "conversational",
                "content_elements": "value proposition and call-to-action",
                "num_hashtags": 3,
                "platform_specific_instructions": "Follow platform best practices",
                "additional_requirements": ""
            },
            examples=[
                {
                    "platform": "LinkedIn",
                    "topic": "AI in Marketing",
                    "target_audience": "marketing professionals",
                    "output_sample": "🚀 AI is revolutionizing marketing in ways we never imagined..."
                }
            ]
        )
        
        # Email Template
        email_template = ContentTemplate(
            content_type=ContentType.EMAIL,
            template_name="professional_email",
            prompt_template="""
            Write a {email_type} email for {purpose}.
            
            Email Details:
            - Type: {email_type}
            - Purpose: {purpose}
            - Recipient: {recipient}
            - Tone: {tone}
            - Length: {length}
            
            Email Structure:
            1. Subject Line: Compelling and clear
            2. Greeting: Professional and appropriate
            3. Opening: Context and purpose
            4. Body: {body_structure}
            5. Call-to-Action: Clear next steps
            6. Closing: Professional sign-off
            
            Requirements:
            - Maintain {tone} tone throughout
            - Be concise and scannable
            - Include clear value proposition
            - End with specific call-to-action
            
            {specific_instructions}
            """.strip(),
            required_params=["email_type", "purpose", "recipient"],
            optional_params=["tone", "length", "body_structure", "specific_instructions"],
            default_config={
                "tone": "professional",
                "length": "concise",
                "body_structure": "main points with supporting details",
                "specific_instructions": ""
            },
            examples=[
                {
                    "email_type": "follow-up",
                    "purpose": "client meeting recap",
                    "recipient": "potential client",
                    "output_sample": "Subject: Thank you for your time today - Next steps..."
                }
            ]
        )
        
        # Product Description Template
        product_description_template = ContentTemplate(
            content_type=ContentType.PRODUCT_DESCRIPTION,
            template_name="compelling_product_description",
            prompt_template="""
            Create a compelling product description for {product_name}.
            
            Product Information:
            - Product: {product_name}
            - Category: {product_category}
            - Target Customer: {target_customer}
            - Key Features: {key_features}
            - Benefits: {main_benefits}
            - Price Point: {price_range}
            
            Description Structure:
            1. Attention-grabbing headline
            2. Problem/need identification
            3. Solution presentation (product introduction)
            4. Key features and benefits
            5. Social proof or credibility indicators
            6. Call-to-action
            
            Writing Requirements:
            - Length: {word_count} words
            - Tone: {tone}
            - Focus on benefits over features
            - Use sensory language and emotional triggers
            - Include relevant keywords for SEO
            - Address common objections
            
            {additional_specs}
            """.strip(),
            required_params=["product_name", "product_category", "target_customer"],
            optional_params=["key_features", "main_benefits", "price_range", "word_count", "tone", "additional_specs"],
            default_config={
                "word_count": 200,
                "tone": "persuasive",
                "key_features": "main product features",
                "main_benefits": "primary customer benefits",
                "price_range": "competitive pricing",
                "additional_specs": ""
            },
            examples=[
                {
                    "product_name": "Wireless Bluetooth Headphones",
                    "product_category": "Electronics",
                    "target_customer": "music enthusiasts",
                    "output_sample": "Experience crystal-clear audio with our premium wireless headphones..."
                }
            ]
        )
        
        # Article Template
        article_template = ContentTemplate(
            content_type=ContentType.ARTICLE,
            template_name="authoritative_article",
            prompt_template="""
            Write an authoritative article about {topic} for {publication_type}.
            
            Article Specifications:
            - Topic: {topic}
            - Publication: {publication_type}
            - Target Audience: {target_audience}
            - Word Count: {word_count}
            - Tone: {tone}
            - Expertise Level: {expertise_level}
            
            Article Structure:
            1. Compelling headline with keyword
            2. Executive summary or abstract
            3. Introduction with thesis statement
            4. {num_main_sections} main sections with evidence
            5. Case studies or examples
            6. Conclusion with implications
            7. References or sources (if applicable)
            
            Content Requirements:
            - Include relevant statistics and data
            - Cite credible sources
            - Provide actionable insights
            - Use subheadings for readability
            - Include expert quotes or perspectives
            - Address counterarguments
            
            {research_requirements}
            """.strip(),
            required_params=["topic", "publication_type", "target_audience"],
            optional_params=["word_count", "tone", "expertise_level", "num_main_sections", "research_requirements"],
            default_config={
                "word_count": 1500,
                "tone": "authoritative",
                "expertise_level": "intermediate",
                "num_main_sections": 4,
                "research_requirements": "Include recent data and expert opinions"
            },
            examples=[
                {
                    "topic": "Future of Artificial Intelligence",
                    "publication_type": "technology magazine",
                    "target_audience": "tech professionals",
                    "output_sample": "The AI Revolution: How Machine Learning is Reshaping Industries..."
                }
            ]
        )
        
        # Store templates
        self.templates = {
            "blog_post": blog_post_template,
            "social_media": social_media_template,
            "email": email_template,
            "product_description": product_description_template,
            "article": article_template
        }
    
    def get_template(self, template_name: str) -> Optional[ContentTemplate]:
        """Get a template by name."""
        return self.templates.get(template_name)
    
    def list_templates(self) -> List[str]:
        """List all available template names."""
        return list(self.templates.keys())
    
    def generate_prompt(self, 
                       template_name: str, 
                       parameters: Dict[str, Any]) -> str:
        """
        Generate a prompt using a template and parameters.
        
        Args:
            template_name: Name of the template to use
            parameters: Dictionary of parameters to fill in the template
            
        Returns:
            Generated prompt string
            
        Raises:
            ValueError: If template not found or required parameters missing
        """
        
        template = self.get_template(template_name)
        if not template:
            raise ValueError(f"Template '{template_name}' not found")
        
        # Check required parameters
        missing_params = [param for param in template.required_params 
                         if param not in parameters]
        if missing_params:
            raise ValueError(f"Missing required parameters: {missing_params}")
        
        # Merge with defaults
        final_params = {**template.default_config, **parameters}
        
        # Format the template
        try:
            prompt = template.prompt_template.format(**final_params)
            return prompt
        except KeyError as e:
            raise ValueError(f"Parameter {e} not provided and no default available")
    
    def get_template_info(self, template_name: str) -> Dict[str, Any]:
        """Get information about a template."""
        
        template = self.get_template(template_name)
        if not template:
            raise ValueError(f"Template '{template_name}' not found")
        
        return {
            "name": template.template_name,
            "content_type": template.content_type.value,
            "required_params": template.required_params,
            "optional_params": template.optional_params,
            "defaults": template.default_config,
            "examples": template.examples
        }
    
    def validate_parameters(self, 
                           template_name: str, 
                           parameters: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate parameters for a template.
        
        Returns:
            Dictionary with validation results
        """
        
        template = self.get_template(template_name)
        if not template:
            return {"valid": False, "error": f"Template '{template_name}' not found"}
        
        # Check required parameters
        missing_required = [param for param in template.required_params 
                           if param not in parameters]
        
        # Check for unknown parameters
        all_params = set(template.required_params + template.optional_params)
        unknown_params = [param for param in parameters 
                         if param not in all_params]
        
        valid = len(missing_required) == 0
        
        return {
            "valid": valid,
            "missing_required": missing_required,
            "unknown_params": unknown_params,
            "provided_params": list(parameters.keys()),
            "all_available_params": list(all_params)
        }
    
    def create_custom_template(self, 
                              template_name: str,
                              content_type: ContentType,
                              prompt_template: str,
                              required_params: List[str],
                              optional_params: List[str] = None,
                              default_config: Dict[str, Any] = None,
                              examples: List[Dict[str, str]] = None) -> ContentTemplate:
        """Create and register a custom template."""
        
        custom_template = ContentTemplate(
            content_type=content_type,
            template_name=template_name,
            prompt_template=prompt_template,
            required_params=required_params,
            optional_params=optional_params or [],
            default_config=default_config or {},
            examples=examples or []
        )
        
        self.templates[template_name] = custom_template
        return custom_template
    
    def export_template(self, template_name: str, filepath: str):
        """Export a template to a JSON file."""
        
        template = self.get_template(template_name)
        if not template:
            raise ValueError(f"Template '{template_name}' not found")
        
        template_data = {
            "content_type": template.content_type.value,
            "template_name": template.template_name,
            "prompt_template": template.prompt_template,
            "required_params": template.required_params,
            "optional_params": template.optional_params,
            "default_config": template.default_config,
            "examples": template.examples
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(template_data, f, indent=2, ensure_ascii=False)
    
    def import_template(self, filepath: str, template_name: str = None):
        """Import a template from a JSON file."""
        
        with open(filepath, 'r', encoding='utf-8') as f:
            template_data = json.load(f)
        
        content_type = ContentType(template_data["content_type"])
        name = template_name or template_data["template_name"]
        
        template = ContentTemplate(
            content_type=content_type,
            template_name=name,
            prompt_template=template_data["prompt_template"],
            required_params=template_data["required_params"],
            optional_params=template_data.get("optional_params", []),
            default_config=template_data.get("default_config", {}),
            examples=template_data.get("examples", [])
        )
        
        self.templates[name] = template
        return template


# Convenience functions for common content types
def generate_blog_post(topic: str, 
                      target_audience: str, 
                      word_count: int = 1000,
                      **kwargs) -> str:
    """Quick function to generate a blog post prompt."""
    
    engine = ContentTemplateEngine()
    params = {
        "topic": topic,
        "target_audience": target_audience,
        "word_count": word_count,
        **kwargs
    }
    
    return engine.generate_prompt("blog_post", params)

def generate_social_media_post(platform: str,
                              topic: str,
                              target_audience: str,
                              **kwargs) -> str:
    """Quick function to generate a social media post prompt."""
    
    engine = ContentTemplateEngine()
    params = {
        "platform": platform,
        "topic": topic,
        "target_audience": target_audience,
        **kwargs
    }
    
    return engine.generate_prompt("social_media", params)

def generate_email(email_type: str,
                  purpose: str,
                  recipient: str,
                  **kwargs) -> str:
    """Quick function to generate an email prompt."""
    
    engine = ContentTemplateEngine()
    params = {
        "email_type": email_type,
        "purpose": purpose,
        "recipient": recipient,
        **kwargs
    }
    
    return engine.generate_prompt("email", params)

def generate_product_description(product_name: str,
                               product_category: str,
                               target_customer: str,
                               **kwargs) -> str:
    """Quick function to generate a product description prompt."""
    
    engine = ContentTemplateEngine()
    params = {
        "product_name": product_name,
        "product_category": product_category,
        "target_customer": target_customer,
        **kwargs
    }
    
    return engine.generate_prompt("product_description", params)


# Example usage and testing
if __name__ == "__main__":
    # Initialize the engine
    engine = ContentTemplateEngine()
    
    # List available templates
    print("Available templates:")
    for template_name in engine.list_templates():
        print(f"- {template_name}")
    
    # Generate a blog post prompt
    blog_params = {
        "topic": "Sustainable Web Development",
        "target_audience": "web developers",
        "word_count": 1200,
        "tone": "professional",
        "key_points": "energy efficiency, green hosting, optimized code",
        "seo_keywords": "sustainable web development, green coding, eco-friendly websites"
    }
    
    blog_prompt = engine.generate_prompt("blog_post", blog_params)
    print("\nGenerated Blog Post Prompt:")
    print(blog_prompt)
    
    # Generate a social media post prompt
    social_params = {
        "platform": "LinkedIn",
        "topic": "Remote Work Productivity",
        "target_audience": "working professionals",
        "char_limit": 300,
        "tone": "conversational",
        "num_hashtags": 5
    }
    
    social_prompt = engine.generate_prompt("social_media", social_params)
    print("\nGenerated Social Media Prompt:")
    print(social_prompt)
    
    # Validate parameters
    validation = engine.validate_parameters("email", {"email_type": "follow-up"})
    print(f"\nValidation result: {validation}")
    
    # Get template info
    template_info = engine.get_template_info("product_description")
    print(f"\nTemplate info: {template_info}")
