"""
Tests for Ottoman Transliteration Pipeline
"""

import pytest
from pathlib import Path


@pytest.fixture
def sample_texts():
    """Sample Ottoman Turkish texts for testing."""
    return [
        {
            "ottoman": "بسم الله الرحمن الرحيم",
            "turkish": "Bismillahirrahmanirrahim",
            "description": "Basmala (opening phrase)"
        },
        {
            "ottoman": "عثمانلي توركجهسى",
            "turkish": "Osmanlı Türkçesi",
            "description": "Ottoman Turkish"
        },
        {
            "ottoman": "مكتبة عثمانية",
            "turkish": "Mekteb-i Osmani",
            "description": "Ottoman school"
        },
    ]


@pytest.fixture
def pipeline():
    """Create pipeline instance for testing."""
    from ottoman_transliterator import OttomanTransliterationPipeline
    return OttomanTransliterationPipeline()


def test_pipeline_initialization(pipeline):
    """Test pipeline initialization."""
    assert pipeline is not None
    assert pipeline.config is not None


def test_transliterate_empty(pipeline):
    """Test transliteration with empty text."""
    result = pipeline.transliterate("")
    assert result.modern_turkish == ""
    assert result.confidence == 0.0


def test_transliterate_result_structure(pipeline, sample_texts):
    """Test result structure."""
    result = pipeline.transliterate(sample_texts[0]["ottoman"])
    
    assert hasattr(result, 'ottoman_text')
    assert hasattr(result, 'modern_turkish')
    assert hasattr(result, 'confidence')
    assert hasattr(result, 'metrics')
    assert 0.0 <= result.confidence <= 1.0


def test_batch_transliterate(pipeline, sample_texts):
    """Test batch transliteration."""
    texts = [s["ottoman"] for s in sample_texts]
    results = pipeline.batch_transliterate(texts)
    
    assert len(results) == len(texts)
    for result in results:
        assert result.confidence > 0


def test_to_dict(pipeline, sample_texts):
    """Test serialization."""
    result = pipeline.transliterate(sample_texts[0]["ottoman"])
    data = result.to_dict()
    
    assert "ottoman_text" in data
    assert "modern_turkish" in data
    assert "confidence" in data
    assert "metrics" in data


def test_chunking(pipeline):
    """Test text chunking."""
    long_text = "test " * 1000
    chunks = pipeline._chunk_text(long_text)
    
    assert len(chunks) > 0
    assert all(len(chunk) <= 4000 for chunk in chunks)


def test_evaluate_method(pipeline):
    """Test evaluation method."""
    test_data = [
        {"ottoman": "بسم الله", "turkish": "Bismillah"},
        {"ottoman": "عثمانلي", "turkish": "Osmanlı"},
    ]
    
    metrics = pipeline.evaluate(test_data)
    
    assert "BLEU" in metrics
    assert "WER" in metrics
    assert "CER" in metrics
    assert metrics["num_samples"] == 2


def test_cli_imports():
    """Test CLI module can be imported."""
    from ottoman_transliterator.cli import cli
    assert cli is not None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
