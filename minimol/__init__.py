"""Minimol package initializer
"""

__version__ = "0.1.0"
__author__ = "Fahhed"
__email__ = "fahhedhh@gmail.com"

# Re-export public API
from .neural_network import (
    Minimol70B,
    MinimolTrainer,
    RotaryPositionalEmbedding,
    MultiHeadAttention,
    TransformerBlock,
)

from .terminal_ui import (
    TerminalUI,
    UIConfig,
    Theme,
    ThemeConfig,
    ConversationMemory,
    CommandParser,
    ResponseRenderer,
    StatusBar,
)

from .llm_router import (
    LLMRouter,
    LLMConfig,
    ProviderConfig,
    ProviderType,
    UseCase,
    OllamaAdapter,
    ClaudeAdapter,
    OpenAIAdapter,
    GeminiAdapter,
    CostOptimizer,
    FallbackChain,
)

__all__ = [
    "Minimol70B",
    "MinimolTrainer",
    "RotaryPositionalEmbedding",
    "MultiHeadAttention",
    "TransformerBlock",
    "TerminalUI",
    "UIConfig",
    "Theme",
    "ThemeConfig",
    "ConversationMemory",
    "CommandParser",
    "ResponseRenderer",
    "StatusBar",
    "LLMRouter",
    "LLMConfig",
    "ProviderConfig",
    "ProviderType",
    "UseCase",
    "OllamaAdapter",
    "ClaudeAdapter",
    "OpenAIAdapter",
    "GeminiAdapter",
    "CostOptimizer",
    "FallbackChain",
]
