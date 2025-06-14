"""
Prompt Engineering Utilities and Templates for Python

This package provides a comprehensive set of tools for effective prompt engineering,
including templates, evaluation frameworks, and optimization utilities.
"""

# Core imports
from .prompt_builder import PromptBuilder
from .template_engine import TemplateEngine
from .evaluator import PromptEvaluator
from .optimizer import PromptOptimizer

# Template imports
from .templates import (
    ContentTemplate,
    CodeTemplate,
    AnalysisTemplate,
    BusinessTemplate,
    CreativeTemplate
)

# Utility imports
from .utils import (
    TokenCounter,
    CostCalculator,
    ResponseCache,
    ConfigManager
)

# Model imports  
from .models import (
    OpenAIModel,
    AnthropicModel, 
    ModelRegistry
)

__version__ = "1.0.0"
__author__ = "Prompt Engineering Team"

__all__ = [
    # Core classes
    "PromptBuilder",
    "TemplateEngine", 
    "PromptEvaluator",
    "PromptOptimizer",
    
    # Templates
    "ContentTemplate",
    "CodeTemplate",
    "AnalysisTemplate", 
    "BusinessTemplate",
    "CreativeTemplate",
    
    # Utilities
    "TokenCounter",
    "CostCalculator",
    "ResponseCache", 
    "ConfigManager",
    
    # Models
    "OpenAIModel",
    "AnthropicModel",
    "ModelRegistry"
]
