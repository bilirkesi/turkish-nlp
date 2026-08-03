# Osmanlica-Bench-v1 Dataset

## Overview

Benchmark dataset for evaluating Ottoman Turkish transliteration systems.

### Statistics

- **Total samples**: 6,500
- **Train**: 5,000 (77%)
- **Validation**: 500 (7.7%)
- **Test**: 1,000 (15.3%)
- **Average length**: 450 chars/sample

### Sources

- Servet-i Funun (1896-1901)
- Ruznamçe Registers (17th century)
- TBMM Proceedings (1920s)
- OTC Corpus samples

### Metrics

| Metric | Value |
|--------|-------|
| CER | 6.46% |
| WER | 20.69% |
| BLEU | 77.18 |

### Usage

```python
from datasets import load_dataset

dataset = load_dataset("bilirkesi/osmanlica-bench-v1")
print(dataset["test"][0])
```

### License

MIT License

### Citation

```bibtex
@misc{osmanlica2026,
  title={Osmanlica-Bench-v1: Benchmark Dataset for Ottoman Turkish Transliteration},
  author={Bilirkesi AI Team},
  year={2026},
  url={https://huggingface.co/datasets/bilirkesi/osmanlica-bench-v1}
}
```
