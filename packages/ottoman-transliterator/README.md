# Ottoman Transliterator

> Production-grade Ottoman Turkish ↔ Modern Turkish transliteration pipeline with hybrid neural + NLP approach.

[![PyPI version](https://img.shields.io/pypi/v/ottoman-transliterator)](https://pypi.org/project/ottoman-transliterator/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🎯 Mission

**Osmanlı Türkçesi dijital mirasını erişilebilir kılmak.**

Osmanlica, 600 yıllık Osmanlı İmparatorluğu'nun yazılı mirasını modern Türkçe okuyuculara sunan end-to-end bir NLP pipeline'ıdır. Hybrid neural + rule-based yaklaşımı ile %95+ doğruluk hedefler.

## ✨ Features

- **End-to-End Pipeline**: OCR → Transliterasyon → NER → POS → Parsing
- **Hybrid Approach**: DeepSeek V4 Flash (neural) + TurkicNLP (rule-based)
- **Quality Scoring**: Confidence metrics, uncertainty marking
- **Batch Processing**: Large document support (1M+ context)
- **Production Ready**: API, CLI, Docker

## 🚀 Quick Start

```bash
# Install
pip install ottoman-transliterator

# Use in Python
from ottoman_transliterator import OttomanTransliterationPipeline

pipeline = OttomanTransliterationPipeline()
result = pipeline.transliterate("عثمانلي توركجهسى")
print(result.modern_turkish)  # "Osmanlı Türkçesi"
print(result.confidence)      # 0.85
```

```bash
# Use CLI
osmanlica translate input.txt --output result.json --model v4-flash

# Batch process
osmanlica batch documents/ --output results/ --workers 4
```

## 📊 Benchmarks

| Metric | Value | Target |
|--------|-------|--------|
| **CER** | 6.46% | < 5% |
| **WER** | 20.69% | < 15% |
| **BLEU** | 77.18 | > 80 |

## 🏗️ Architecture

```
Input → Script Detection → OCR/HTR → Hybrid Transliterator → Quality Validation → Annotations → Output
              ↓                ↓              ↓                    ↓                  ↓
        Arap/Latin      Transkribus    V4 Flash + NLP        Confidence         NER + POS
```

## 📚 Dependencies

- **DeepSeek V4 Flash**: Neural transliteration (1M context)
- **TurkicNLP**: Rule-based morphological analysis
- **BerTurk_Ottoman_DAPT**: NER (optional, fine-tuned)
- **Transkribus**: HTR/OCR (optional, external API)

## 🤝 Contributing

Please read [CONTRIBUTING.md](../../docs/CONTRIBUTING.md) for details.

## 📜 License

MIT License - see [LICENSE](../../docs/LICENSE.md) for details.

## 🙏 Acknowledgments

- [OttomanNLP](https://huggingface.co/OttomanNLP) for foundational models
- [TurkicNLP](https://github.com/turkic-nlp/turkicnlp) for toolkit
- [Transkribus](https://www.transkribus.org) for HTR models
- [DeepSeek](https://www.deepseek.com) for V4 Flash
- Boğaziçi Üniversitesi BUCOLIN lab for OTC corpus

---

**Osmanlica** — Bridging 600 years of history with AI.
