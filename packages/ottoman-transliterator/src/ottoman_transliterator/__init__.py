"""
Osmanlica Transliteration Package
Production-grade Ottoman Turkish ↔ Modern Turkish transliteration
"""

from .pipeline import (
    OttomanPipelineConfig,
    TransliterationResult,
    OttomanTransliterationPipeline,
)

__version__ = "1.0.0"
__author__ = "Bilirkesi AI Team"
__email__ = "research@bilirkesi.ai"

__all__ = [
    "OttomanPipelineConfig",
    "TransliterationResult",
    "OttomanTransliterationPipeline",
]
