# Turkish NLP - Ottoman Language Processing

**Turkish NLP** is a comprehensive project for Ottoman Turkish language processing, featuring:

1. **Transliteration Pipeline** - Ottoman Turkish ↔ Modern Turkish conversion
2. **Agent Pipeline** - AI agent with tools, models, and session management (see [ottoman-agent-pipeline](https://github.com/bilirkesi/ottoman-agent-pipeline))
3. **Desktop App** - Electron-based desktop application
4. **Mobile App** - React Native mobile application

---

## 📦 Packages

### 1. Ottoman Transliterator
Production-grade transliteration pipeline.

**Install:**
```bash
pip install ottoman-transliterator
```

**Usage:**
```python
from ottoman_transliterator import OttomanTransliterationPipeline

pipeline = OttomanTransliterationPipeline()
result = pipeline.transliterate("عثمانلي توركجهسى")
print(result.modern_turkish)  # "Osmanlı Türkçesi"
```

**Docs:** [packages/ottoman-transliterator/README.md](packages/ottoman-transliterator/README.md)

---

### 2. Ottoman Agent Pipeline
Full-featured AI agent with tools, models, and API.

**Repo:** https://github.com/bilirkesi/ottoman-agent-pipeline

**Usage:**
```python
from ottoman_agent_pipeline import AgentOrchestrator

orch = AgentOrchestrator()
await orch.initialize()

result = await orch.chat("عثمانلي توركجهسى")
print(result.output)
```

**CLI:**
```bash
ottoman-agent chat "عثمانli توركجهسى"
ottoman-agent translate "بسم الله"
ottoman-agent serve --port 8000
```

---

## 🚀 Quick Start

```bash
# Clone
git clone https://github.com/bilirkesi/turkish-nlp.git
cd turkish-nlp

# Install transliterator
pip install -e packages/ottoman-transliterator

# Install agent (separate repo)
cd ../ottoman-agent-pipeline
pip install -e .

# Run demo
python demos/gradio_app.py
```

---

## 📊 Benchmarks

| Metric | Value |
|--------|-------|
| **CER** | 6.46% |
| **WER** | 20.69% |
| **BLEU** | 77.18 |

Full report: [docs/BENCHMARK_REPORT_v1.md](docs/BENCHMARK_REPORT_v1.md)

---

## 🏗️ Architecture

```
turkish-nlp/
├── packages/
│   └── ottoman-transliterator/   # Core transliteration package
├── demos/                        # Gradio demo app
├── docs/                         # Documentation
├── models/                       # Model cards
├── datasets/                     # Dataset cards
└── .github/workflows/            # CI/CD
```

**Agent Pipeline:** https://github.com/bilirkesi/ottoman-agent-pipeline

---

## 🔗 Links

- **GitHub (Main):** https://github.com/bilirkesi/turkish-nlp
- **GitHub (Agent):** https://github.com/bilirkesi/ottoman-agent-pipeline
- **PyPI:** https://pypi.org/project/ottoman-transliterator/
- **HuggingFace Model:** https://huggingface.co/bilirkesi/osmanlica-v1
- **HuggingFace Dataset:** https://huggingface.co/datasets/bilirkesi/osmanlica-bench-v1
- **Zenodo:** https://doi.org/10.5281/zenodo.21781872

---

## 📄 License

MIT License - See [LICENSE.md](LICENSE.md) for details.
