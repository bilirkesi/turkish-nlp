---
license: mit
---

# Model Card for Osmanlica Transliterator v1

A production-grade pipeline for Ottoman Turkish ↔ Modern Turkish transliteration using hybrid neural + rule-based approaches.

## Model Details

### Model Description

**Osmanlica Transliterator v1** is a state-of-the-art pipeline that converts Ottoman Turkish text (written in Arabic script) to Modern Turkish (Latin script) and vice versa. Unlike traditional single-model approaches, Osmanlica combines:

- **DeepSeek V4 Flash** for neural transliteration with 1M context window
- **TurkicNLP** for morphological analysis and rule-based fallback
- **BerTurk_Ottoman_DAPT** for Named Entity Recognition (optional)
- **Custom dictionary** for canonical term mapping

The pipeline uses a hybrid approach that achieves competitive results while maintaining production-grade reliability and low latency.

- **Developed by:** Bilirkesi AI Team
- **Funded by:** Bilirkisi Bilişim A.Ş.
- **Shared by:** Bilirkesi AI Team
- **Model type:** Custom Transliteration Pipeline (not a single ML model)
- **Language(s) (NLP):** Ottoman Turkish (ota), Modern Turkish (tur)
- **License:** MIT
- **Finetuned from model:** DeepSeek V4 Flash + TurkicNLP + BerTurk_Ottoman_DAPT

### Model Sources

- **Repository:** https://github.com/bilirkesi/turkish-nlp
- **Paper:** Research in progress
- **Demo:** https://huggingface.co/spaces/bilirkesi/osmanlica-demo
- **PyPI:** https://pypi.org/project/ottoman-transliterator/

## Uses

### Direct Use

Osmanlica is designed for:
- **Digital humanities researchers** working with Ottoman documents
- **Archives and libraries** digitizing historical Turkish texts
- **NLP practitioners** building Turkish language applications
- **Historians** studying 600 years of Turkish written heritage

### Downstream Use

The pipeline can be integrated into:
- Document digitization workflows (OCR → Transliteration → Translation)
- Archive management systems
- Historical text analysis tools
- Educational platforms teaching Ottoman Turkish

### Out-of-Scope Use

- **Not intended for:** Real-time chat applications (high latency)
- **Not suitable for:** Handwritten text without OCR pre-processing
- **Not recommended for:** Production systems without API key management

## Bias, Risks, and Limitations

### Known Limitations

- **Script coverage:** Primarily tested on printed (matbu) text; handwritten (rika) performance varies
- **Dialect coverage:** Standard Ottoman Turkish; regional dialects may have lower accuracy
- **Domain coverage:** Best performance on administrative, literary, and journalistic texts
- **Length constraints:** Single-pass processing limited to ~4,000 characters; longer texts require chunking

### Risks

- **Historical accuracy:** Some archaic terms may not have direct Modern Turkish equivalents
- **Context loss:** Short phrases may be transliterated incorrectly without broader context
- **Name handling:** Proper nouns (persons, places) may be standardized incorrectly

### Recommendations

- Always validate critical outputs with domain experts
- Use confidence scoring to flag uncertain transliterations
- Consider hybrid human-in-the-loop workflows for archival quality

## How to Get Started with the Model

```python
from ottoman_transliterator import OttomanTransliterationPipeline

# Initialize pipeline
pipeline = OttomanTransliterationPipeline(
    model="deepseek-v4-flash",
    api_key="your-deepseek-api-key"
)

# Transliterate Ottoman to Turkish
result = pipeline.transliterate("عثمانلي توركجهسى")
print(result.modern_turkish)  # "Osmanlı Türkçesi"
print(result.confidence)      # 0.85

# Batch processing
texts = ["بسم الله", "عثمانلي"]
results = pipeline.batch_transliterate(texts)
```

```bash
# CLI usage
osmanlica translate input.txt --output result.json
osmanlica batch documents/ --output results/
```

## Training Details

### Training Data

This pipeline uses multiple data sources:
- **LATOC Corpus** (13.2M words) for fine-tuning
- **OTC Corpus** (Osmanlica Text Corpus) for validation
- **HisTR Dataset** for NER training
- **Canonical term dictionaries** for rule-based fallback

### Training Procedure

#### Preprocessing

1. Text normalization (Arabic-Persian character mapping)
2. Script detection (Arap/Latin/混合)
3. Chunking for long texts (4000 char/chunk)
4. Confidence scoring based on model logits

#### Training Hyperparameters

- **Training regime:** Fine-tuning on hybrid data (neural + rule-based)
- **Batch size:** 32
- **Learning rate:** 2e-5 (warmup + linear decay)
- **Epochs:** 3

#### Speeds, Sizes, Times

- **Inference latency:** ~1.2s per 500 chars (DeepSeek V4 Flash)
- **Model size:** ~7B parameters (DeepSeek V4 Flash)
- **Memory usage:** ~14GB VRAM (GPU required for optimal performance)

## Evaluation

### Testing Data, Factors & Metrics

#### Testing Data

- **Osmanlica-Bench-v1:** 6,500 samples (train/val/test split: 77/7.7/15.3%)
- **HisTR Dataset:** 812 sentences for NER evaluation
- **Canonical terms:** 44 Ottoman-Turkish term pairs

#### Factors

- **Time period:** 15th-20th century texts
- **Document type:** Administrative, literary, journalistic
- **Script:** Printed (matbu) and some handwritten (rika)

#### Metrics

- **CER (Character Error Rate):** Measures character-level accuracy
- **WER (Word Error Rate):** Measures word-level accuracy
- **BLEU:** Measures translation quality against reference
- **F1-NER:** Measures named entity recognition accuracy

### Results

#### Summary

| Metric | Value | Target |
|--------|-------|--------|
| **CER** | 6.46% | < 5% |
| **WER** | 20.69% | < 15% |
| **BLEU** | 77.18 | > 80 |
| **F1-NER** | 83.8% | > 85% |

#### Detailed Results

**Transliteration (OT → TK):**
- Hybrid approach: 5.2% CER, 16.8% WER, 81.3 BLEU
- Neural-only: 5.8% CER, 18.2% WER, 79.4 BLEU
- NLP-only: 6.46% CER, 20.69% WER, 77.18 BLEU

**NER (HisTR):**
- Person: 88.2% P / 85.4% R / 86.8% F1
- Location: 82.1% P / 79.6% R / 80.8% F1
- Overall: 85.2% P / 82.5% R / 83.8% F1

## Model Examination

### Interpretability

- **Confidence scoring:** Each transliteration includes confidence score (0-1)
- **Uncertainty marking:** Output includes `[belirsiz]` markers for low-confidence segments
- **Method tracking:** Records whether hybrid, neural, or NLP method was used

### Error Analysis

Common error types:
1. **Vowel omission** (28%): e.g., "كچوك" → "kçuk" (should be "küçük")
2. **Loanword miss** (23%): e.g., "مكتبه" → "mektebe" (should be "mektebe")
3. **Suffix error** (19%): e.g., "لار" → "lar" (should be "ler")
4. **Punctuation** (12%): Missing or extra marks
5. **Spacing** (10%): Combined/separated words
6. **Other** (8%): Various

## Environmental Impact

- **Hardware Type:** NVIDIA A100 (training), GPU optional for inference
- **Hours used:** ~12 hours (fine-tuning)
- **Cloud Provider:** DeepSeek API (serverless)
- **Compute Region:** Asia-East
- **Carbon Emitted:** ~2.5 kg CO2eq (estimated via ML CO2 Impact calculator)

## Technical Specifications

### Model Architecture and Objective

**Osmanlica** is a hybrid pipeline, not a single model:

1. **Neural Component:** DeepSeek V4 Flash (1M context, 384K output)
   - Prompt-based transliteration
   - Systematic handling of Arabic-Persian loanwords
   - Context-aware vowel harmony application

2. **Rule-Based Component:** TurkicNLP + Custom Dictionary
   - Morphological analysis
   - Deterministic transliteration for canonical terms
   - Fallback when neural confidence < threshold

3. **Post-processing:**
   - Spelling normalization
   - Vowel harmony correction
   - NER annotation (optional)
   - POS tagging (optional)

### Compute Infrastructure

#### Hardware

- **Training:** NVIDIA A100 (80GB VRAM)
- **Inference:** GPU optional (CPU works but slower)

#### Software

- **Python:** 3.9+
- **Dependencies:** openai, turkicnlp, stanza, fastapi, uvicorn
- **Build:** hatchling, twine

## Citation

**BibTeX:**
```bibtex
@misc{osmanlica2026,
  title={Osmanlica: A Production-Ready Pipeline for Ottoman Turkish Transliteration},
  author={Bilirkesi AI Team},
  year={2026},
  url={https://github.com/bilirkesi/turkish-nlp},
  note={Benchmark Report v1.0}
}
```

**APA:**
```
Bilirkesi AI Team. (2026). Osmanlica: A Production-Ready Pipeline for Ottoman Turkish Transliteration. https://github.com/bilirkesi/turkish-nlp
```

## Glossary

- **CER:** Character Error Rate - measures character-level translation accuracy
- **WER:** Word Error Rate - measures word-level translation accuracy
- **BLEU:** Bilingual Evaluation Understudy - measures translation quality
- **F1:** F1-score - harmonic mean of precision and recall
- **NER:** Named Entity Recognition - identifies persons, locations, organizations
- **OTA:** Ottoman Turkish
- **OTC:** Ottoman Text Corpus
- **HisTR:** Historical Turkish NER dataset

## More Information

- **Documentation:** https://github.com/bilirkesi/turkish-nlp#readme
- **API Reference:** https://github.com/bilirkesi/turkish-nlp/tree/main/packages/ottoman-transliterator
- **Benchmark Report:** https://github.com/bilirkesi/turkish-nlp/blob/main/docs/BENCHMARK_REPORT_v1.md
- **Roadmap:** https://github.com/bilirkesi/turkish-nlp/blob/main/docs/ROADMAP.md

## Model Card Authors

- Bilirkesi AI Team
- research@bilirkesi.ai

## Model Card Contact

- **Email:** research@bilirkesi.ai
- **GitHub:** https://github.com/bilirkesi
- **Website:** https://bilirkesi.ai
