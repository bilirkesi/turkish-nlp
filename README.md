# Turkish NLP

> High-quality, production-ready NLP tools for Turkish language processing.

## 📦 Packages

### ottoman-transliterator

Production-grade Ottoman Turkish ↔ Modern Turkish transliteration pipeline.

[![PyPI version](https://img.shields.io/pypi/v/ottoman-transliterator)](https://pypi.org/project/ottoman-transliterator/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Features:**
- Hybrid neural + rule-based transliteration
- DeepSeek V4 Flash integration
- TurkicNLP morphological analysis
- Confidence scoring & uncertainty marking
- Batch processing support
- REST API + CLI

**Quick Start:**
```bash
pip install ottoman-transliterator
```

```python
from ottoman_transliterator import OttomanTransliterationPipeline

pipeline = OttomanTransliterationPipeline()
result = pipeline.transliterate("عثمانلي توركجهسى")
print(result.modern_turkish)  # "Osmanlı Türkçesi"
print(result.confidence)      # 0.85
```

**Documentation:** [packages/ottoman-transliterator/README.md](./packages/ottoman-transliterator/README.md)

---

## 🏗️ Repository Structure

```
turkish-nlp/
├── packages/
│   └── ottoman-transliterator/   # Ottoman Turkish transliteration
│       ├── src/
│       │   └── ottoman_transliterator/
│       │       ├── __init__.py
│       │       ├── pipeline.py
│       │       └── cli.py
│       ├── tests/
│       │   └── test_pipeline.py
│       ├── docs/
│       ├── pyproject.toml
│       ├── requirements.txt
│       ├── Dockerfile
│       └── README.md
├── docs/                         # Documentation
│   ├── LICENSE.md
│   ├── CONTRIBUTING.md
│   └── BENCHMARK_REPORT_v1.md
├── .github/
│   └── workflows/
│       ├── build-publish.yml
│       └── docker-publish.yml
└── README.md
```

---

## 📊 Benchmarks

| Metric | Value | Target |
|--------|-------|--------|
| **CER** | 6.46% | < 5% |
| **WER** | 20.69% | < 15% |
| **BLEU** | 77.18 | > 80 |

*Full benchmark report: [docs/BENCHMARK_REPORT_v1.md](./docs/BENCHMARK_REPORT_v1.md)*

---

## 🚀 Contributing

Please read [docs/CONTRIBUTING.md](./docs/CONTRIBUTING.md) for details.

---

## 📜 License

This project is licensed under the MIT License - see [docs/LICENSE.md](./docs/LICENSE.md) for details.

---

**Turkish NLP** — Advanced NLP tools for Turkish language processing.
