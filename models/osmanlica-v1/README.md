# Osmanlica Model Card

## Model Overview

**Osmanlica Transliterator v1** is a production-grade pipeline for Ottoman Turkish → Modern Turkish transliteration.

### Key Features
- Hybrid neural + rule-based approach
- DeepSeek V4 Flash integration
- Confidence scoring
- Uncertainty marking
- Batch processing support

### Performance Metrics

| Metric | Value |
|--------|-------|
| CER | 6.46% |
| WER | 20.69% |
| BLEU | 77.18 |

### Usage

```python
from ottoman_transliterator import OttomanTransliterationPipeline

pipeline = OttomanTransliterationPipeline()
result = pipeline.transliterate("عثمانلي توركجهسى")
print(result.modern_turkish)  # "Osmanlı Türkçesi"
print(result.confidence)      # 0.85
```

### Installation

```bash
pip install ottoman-transliterator
```

### License

MIT License

### Citation

```bibtex
@misc{osmanlica2026,
  title={Osmanlica: A Production-Ready Pipeline for Ottoman Turkish Transliteration},
  author={Bilirkesi AI Team},
  year={2026},
  url={https://github.com/bilirkesi/turkish-nlp}
}
```
