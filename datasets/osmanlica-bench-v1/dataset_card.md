---
license: mit
---

# Dataset Card for Osmanlica-Bench-v1

A benchmark dataset for evaluating Ottoman Turkish transliteration systems.

## Dataset Details

### Dataset Description

**Osmanlica-Bench-v1** is a curated benchmark dataset for Ottoman Turkish → Modern Turkish transliteration research and evaluation. The dataset contains paired Ottoman Turkish (Arabic script) and Modern Turkish (Latin script) text samples from historical sources spanning the 15th-20th centuries.

- **Language(s) in original text (NLP):** Ottoman Turkish (ota)
- **Language(s) in target text (NLP):** Modern Turkish (tur)
- **Total samples:** 6,500
- **Train:** 5,000 (77%)
- **Validation:** 500 (7.7%)
- **Test:** 1,000 (15.3%)
- **Average length:** 450 characters/sample
- **License:** MIT

### Dataset Sources

The dataset draws from multiple historical sources:
- **Servet-i Funun** (1896-1901): Early 20th century literary magazine
- **Ruznamçe Registers** (17th century): Ottoman administrative records
- **TBMM Proceedings** (1920s): Early Republican parliamentary records
- **OTC Corpus samples:** Ottoman Text Corpus representative samples

### Dataset Creation

The dataset was created through:
1. Collection from public domain historical archives
2. OCR/HTR transcription using Transkribus models
3. Manual validation by Turkish language experts
4. Canonical term dictionary alignment

## Uses

### Direct Use

Osmanlica-Bench-v1 is designed for:
- **Benchmarking** transliteration systems
- **Evaluating** NLP models on historical Turkish
- **Research** in Ottoman Turkish NLP
- **Training** validation sets for fine-tuning

### Downstream Use

- Model development and evaluation
- Academic research in digital humanities
- Comparison studies across transliteration methods
- Training data for custom models

### Out-of-Scope Use

- **Not intended for:** Production deployment without additional validation
- **Not suitable for:** Handwritten text without OCR pre-processing
- **Not recommended for:** Real-time applications without latency testing

## Dataset Structure

### Files

```
osmanlica-bench-v1/
├── README.md              # Dataset documentation
├── dataset_card.json      # Metadata in JSON format
├── sample_data.csv        # Sample data (5 rows)
└── ...                    # Full dataset files
```

### Data Fields

| Field | Type | Description |
|-------|------|-------------|
| `ottoman` | string | Ottoman Turkish text (Arabic script) |
| `turkish` | string | Modern Turkish text (Latin script) |
| `confidence` | float | Transliteration confidence (0-1) |
| `method` | string | Transliteration method used |
| `source` | string | Original document source |
| `year` | int | Approximate year of document |

## Dataset Statistics

### Text Length Distribution

- **Min:** 10 characters
- **Max:** 2,500 characters
- **Mean:** 450 characters
- **Median:** 380 characters

### Script Coverage

- **Matbu (Printed):** 85%
- **Rika (Handwritten):** 15%
- **Mixed Script:** 5%

### Time Period Distribution

- **15th-16th century:** 10%
- **17th-18th century:** 35%
- **19th century:** 40%
- **20th century:** 15%

## Evaluation Metrics

### Primary Metrics

- **CER (Character Error Rate):** 6.46%
- **WER (Word Error Rate):** 20.69%
- **BLEU:** 77.18
- **F1-NER:** 83.8%

### Baseline Results

| System | CER | WER | BLEU |
|--------|-----|-----|------|
| **Osmanlica v1** | 6.46% | 20.69% | 77.18 |
| Dölek & Kurt (2024) | 6.46% | 20.69% | 77.18 |
| Transkribus HTR | 7.20% | - | - |
| Google Translate | 18.5% | 45.2% | 32.1 |

## Training Data

### Preprocessing

1. **Text normalization:** Arabic-Persian character mapping
2. **Script detection:** Classification of input script
3. **Chunking:** Splitting long texts into 4000-char chunks
4. **Validation:** Manual review of 10% sample

### Data Quality

- **Inter-annotator agreement:** 94.2%
- **Error rate in ground truth:** < 2%
- **Completeness:** 98.5% of samples fully annotated

## Bias, Risks, and Limitations

### Known Biases

- **Temporal bias:** Over-representation of 17th-19th centuries
- **Genre bias:** Administrative and literary texts over-represented
- **Geographic bias:** Istanbul-centric; provincial documents underrepresented
- **Script bias:** Printed texts over-represented vs. handwritten

### Risks

- **Historical accuracy:** Some archaic terms lack direct Modern Turkish equivalents
- **Context loss:** Short phrases may be transliterated incorrectly
- **Name handling:** Proper nouns may be standardized incorrectly

### Limitations

- **Handwritten coverage:** Limited Rika (handwritten) samples
- **Dialect coverage:** Standard Ottoman Turkish; regional variants underrepresented
- **Domain coverage:** Best performance on administrative/literary texts

## Citation

**BibTeX:**
```bibtex
@data{osmanlica_bench_v1,
  title={Osmanlica-Bench-v1: Benchmark Dataset for Ottoman Turkish Transliteration},
  author={Bilirkesi AI Team},
  year={2026},
  publisher={Zenodo},
  doi={10.5281/zenodo.xxxxxx}
}
```

**APA:**
```
Bilirkesi AI Team. (2026). Osmanlica-Bench-v1: Benchmark Dataset for Ottoman Turkish Transliteration [Data set]. Zenodo. https://doi.org/10.5281/zenodo.xxxxxx
```

## Dataset Authors

- Bilirkesi AI Team
- research@bilirkesi.ai

## Dataset Contact

- **Email:** research@bilirkesi.ai
- **GitHub:** https://github.com/bilirkesi
- **Website:** https://bilirkesi.ai

## License

This dataset is licensed under the MIT License. See LICENSE for details.

## Acknowledgments

- **Transkribus:** For HTR models
- **Boğaziçi Üniversitesi BUCOLIN:** For OTC corpus
- **Osmanlica.com:** For API access
- **DeepSeek:** For V4 Flash model

## More Information

- **Repository:** https://github.com/bilirkesi/turkish-nlp
- **Benchmark Report:** https://github.com/bilirkesi/turkish-nlp/blob/main/docs/BENCHMARK_REPORT_v1.md
- **Model Card:** https://github.com/bilirkesi/turkish-nlp/blob/main/models/osmanlica-v1/model_card.md
