---
license: mit
language:
- tr
tags:
- ottoman-turkish
- turkish
- transliteration
- benchmark
- dataset
---

# Osmanlica-Bench-v1

A benchmark dataset for Ottoman Turkish transliteration systems.

## Quick Start

```python
from datasets import load_dataset

dataset = load_dataset("bilirkesi/osmanlica-bench-v1")
print(dataset["test"][0])
```

## Installation

```bash
pip install datasets
```

## Documentation

- [GitHub](https://github.com/bilirkesi/turkish-nlp)
- [Benchmark Report](https://github.com/bilirkesi/turkish-nlp/blob/main/docs/BENCHMARK_REPORT_v1.md)
