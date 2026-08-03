# Contributing to Turkish NLP

First off, thank you for considering contributing to Turkish NLP! It's people like you that make Turkish NLP such a great tool for the digital humanities community.

## 🌟 Code of Conduct

This project and everyone participating in it is governed by the Code of Conduct. By participating, you are expected to uphold this code.

## 📋 How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the issue list as you might find that you don't need to create one. When you are creating a bug report, please include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps which reproduce the problem**
- **Provide specific examples to demonstrate the steps**
- **Describe the behavior you observed and expected**
- **Include screenshots if applicable**
- **Include details about your environment** (OS, Python version, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement request, please include:

- **Use a clear and descriptive title**
- **Provide a step-by-step description of the suggested enhancement**
- **Provide specific examples to demonstrate the steps**
- **Describe the current behavior and the behavior you希望 to see**
- **Explain why this enhancement would be useful**

### Pull Requests

- Fill in the required template
- Do not include issue numbers in the PR title
- Include screenshots and animated GIFs in your pull request whenever possible
- Follow the JavaScript/Python styleguides
- Include thoughtfully-worded, well-structured tests
- Document new code
- End all files with a newline

## 🚀 Development Setup

### Prerequisites

- Python 3.9+
- Git

### Package Development

```bash
# Clone repository
git clone https://github.com/bilirkesi/turkish-nlp.git
cd turkish-nlp

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

# Install package in development mode
pip install -e packages/ottoman-transliterator[dev]

# Run tests
pytest packages/ottoman-transliterator/tests/

# Build package
cd packages/ottoman-transliterator
python -m build
```

## 📝 Coding Standards

### Python

- Follow [PEP 8](https://pep8.org/)
- Use [Black](https://black.readthedocs.io/) for code formatting
- Use [Ruff](https://docs.astral.sh/ruff/) for linting
- Type hints for all functions
- Docstrings for all public APIs

## 🧪 Testing

```bash
# Run all tests
pytest packages/ottoman-transliterator/tests/ -v

# Run with coverage
pytest packages/ottoman-transliterator/tests/ --cov=ottoman_transliterator --cov-report=html

# Run specific test
pytest packages/ottoman-transliterator/tests/test_pipeline.py -v
```

## 📚 Documentation

- Use Sphinx for API docs
- Update README.md for user-facing changes
- Add examples in `docs/examples/`

## 🔄 Git Workflow

1. Create a branch from `main`
2. Make your changes
3. Run tests and linting
4. Commit with [conventional commits](https://www.conventionalcommits.org/)
5. Push and create PR

### Commit Messages

```
feat: add Ottoman NER support
fix: correct transliteration of Arabic loanwords
docs: update API documentation
test: add benchmark tests for WER metric
chore: update dependencies
```

## 🤝 Community

- Join our [Discord](https://discord.gg/turkish-nlp)
- Follow us on [Twitter](https://twitter.com/turkishnlp)

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.
