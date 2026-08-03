---
license: mit
language:
- tr
tags:
- ottoman-turkish
- turkish
- transliteration
- nlp
- historical
- digital-humanities
---

# Osmanlica Transliterator v1

A production-grade pipeline for Ottoman Turkish ↔ Modern Turkish transliteration.

## Quick Start

```python
from ottoman_transliterator import OttomanTransliterationPipeline

pipeline = OttomanTransliterationPipeline()
result = pipeline.transliterate("عثمانلي توركجهسى")
print(result.modern_turkish)  # "Osmanlı Türkçesi"
print(result.confidence)      # 0.85
```

## Installation

```bash
pip install ottoman-transliterator
```

## Documentation

- [GitHub](https://github.com/bilirkesi/turkish-nlp)
- [PyPI](https://pypi.org/project/ottoman-transliterator/)
- [Benchmark Report](https://github.com/bilirkesi/turkish-nlp/blob/main/docs/BENCHMARK_REPORT_v1.md)
