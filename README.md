# Minimol: Multi-Provider LLM Router with Terminal UI

[![Mobile Edition](https://img.shields.io/badge/Mobile%20Edition-Lightweight%20%26%20Powerful-blue?style=flat-square)](README_MOBILE.md)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square)](https://www.python.org/)

A multi-provider LLM router with a Claude-style terminal UI.

---

## Table of Contents

- [Features](#features)
- [Quick Start](#quick-start)
  - [Demo Mode (No LLM Required)](#demo-mode--no-external-llm-required)
  - [Real Inference](#running-real-inference)
  - [Mobile/Low-Resource](#mobiletermux-setup)
- [Installation](#installation)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Development](#development)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

---

## Features

- 🚀 **Multi-provider LLM Router** — Ollama, Claude, OpenAI, Gemini, Mistral, Cohere (config-driven)
- 💻 **Claude-style Terminal UI** — Interactive, real-time responses with rich formatting
- 📱 **Mobile-Friendly Edition** — Lightweight variant for Android/iOS/low-resource devices ([README_MOBILE.md](README_MOBILE.md))
- ⚙️ **Configurable Inference** — YAML-based provider selection, model swapping, API key management
- 🔄 **Async-First Architecture** — Concurrent requests, non-blocking I/O

---

## Quick Start

### Demo Mode (No External LLM Required)

This runs the terminal UI with simulated responses. Works on low-end machines and Termux.

1. **Clone the repo:**

```bash
git clone https://github.com/fahhede-star/Minimol.git
cd Minimol
git checkout reorg/package-structure
```

2. **Create and activate a virtual environment:**

```bash
python3 -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
```

3. **Install the package (UI extras):**

```bash
pip install --upgrade pip setuptools wheel
pip install -e .[ui]
```

4. **Run the terminal UI demo:**

```bash
minimol-ui
# or
python -m minimol.terminal_ui
```

You should see the interactive terminal UI. This demo does not require any model or cloud API keys.

---

### Running Real Inference

The router loads configuration from `config/llm_providers.yaml` by default. Example YAMLs are included at the repo root.

**Recommended: Move YAMLs into `config/` directory:**

```bash
mkdir -p config
cp llm_providers.yaml config/llm_providers.yaml
cp ui.yaml config/ui.yaml
```

**Set environment variables for cloud providers (do not commit keys):**

```bash
export OPENAI_API_KEY="sk-..."
export ANTHROPIC_API_KEY="api-..."
export GEMINI_API_KEY="your-key-here"
```

**Example: Run inference with OpenAI:**

```bash
python -c "import asyncio; from minimol.inference import InferenceEngine; async def r(): \
  e = InferenceEngine(); await e.initialize(); print('ready'); await e.cleanup(); \
  asyncio.run(r())"
```

**Or use the CLI:**

```bash
minimol generate "Explain quantum computing in 2 sentences." --provider openai --model gpt-4
```

**Provider Notes:**
- **Ollama**: Defaults to `http://localhost:11434`; ensure Ollama service is running locally
- **Cloud Providers**: If YAML config references `${ENV_VAR}` for `api_key`, the loader reads the environment variable
- **Model Switching**: Edit `config/llm_providers.yaml` to enable/disable providers and select models

---

### Mobile/Termux Setup

**⚠️ For lightweight mobile installations, see [README_MOBILE.md](README_MOBILE.md) for:**
- ~2-3 min installation (vs 5-10 min)
- ~50-100 MB footprint (vs 100-200 MB)
- ONNX Runtime instead of PyTorch
- Termux-specific setup

**Quick Termux steps:**

```bash
pkg update && pkg upgrade -y
pkg install git python -y

git clone https://github.com/fahhede-star/Minimol.git
cd Minimol
git checkout reorg/package-structure

python -m venv .venv
source .venv/bin/activate

pip install --upgrade pip setuptools wheel
pip install -e .[ui]

# Run the UI demo
python -m minimol.terminal_ui
```

For remote provider access from Termux, set environment variables and ensure your YAML config enables the provider.

---

## Installation

### Full Edition (Desktop/Server)

Includes multi-provider support for cloud-based LLMs.

```bash
pip install -e .[ui]           # Terminal UI only
pip install -e .[ui,openai]    # UI + OpenAI support
pip install -e .[all]          # All providers + dev tools
```

**Installation time:** 5–10 minutes  
**Disk space:** 100–200 MB (no model files required)

### Mobile Edition (Android/Low-Resource)

Lightweight variant with ONNX Runtime instead of PyTorch.

```bash
pip install -e .[mobile]
```

**Installation time:** 2–3 minutes  
**Disk space:** 50–100 MB  
**See:** [README_MOBILE.md](README_MOBILE.md)

### Optional Dependencies

| Extra | Purpose |
|-------|---------|
| `[ui]` | Terminal UI (rich, prompt-toolkit, pygments) |
| `[mobile]` | Lightweight edition (ONNX Runtime, no PyTorch) |
| `[claude]` | Anthropic Claude support |
| `[openai]` | OpenAI support |
| `[google]` | Google Gemini support |
| `[mistral]` | Mistral support |
| `[cohere]` | Cohere support |
| `[dev]` | Development tools (pytest, black, ruff, mypy) |
| `[all]` | All of the above |

---

## Configuration

### File Locations

- **LLM Providers:** `config/llm_providers.yaml`
- **UI Settings:** `config/ui.yaml`
- **Example configs:** Root directory (`llm_providers.yaml`, `ui.yaml`)

### Example: `config/llm_providers.yaml`

```yaml
providers:
  openai:
    enabled: true
    api_key: ${OPENAI_API_KEY}
    model: gpt-4
    temperature: 0.7

  anthropic:
    enabled: true
    api_key: ${ANTHROPIC_API_KEY}
    model: claude-3-sonnet-20240229

  ollama:
    enabled: false
    base_url: http://localhost:11434
    model: mistral

  gemini:
    enabled: false
    api_key: ${GEMINI_API_KEY}
    model: gemini-1.5-pro
```

**Environment Variable Support:** References like `${ENV_VAR}` are resolved at runtime.

---

## Project Structure

```
Minimol/
├── minimol/                       # Main package
│   ├── __init__.py
│   ├── terminal_ui.py             # Claude-style terminal UI
│   ├── inference.py               # InferenceEngine
│   ├── llm_router.py              # Multi-provider LLM router
│   ├── cli.py                     # Command-line interface
│   ├── providers/                 # LLM provider adapters
│   │   ├── __init__.py
│   │   ├── openai_adapter.py      # OpenAI integration
│   │   ├── anthropic_adapter.py   # Claude integration
│   │   ├── ollama_adapter.py      # Ollama local inference
│   │   ├── gemini_adapter.py      # Google Gemini
│   │   └── ...
│   ├── config/                    # Configuration loaders
│   │   ├── __init__.py
│   │   └── loader.py              # YAML config loading
│   └── utils/                     # Utilities
│       ├── __init__.py
│       └── tokenizer.py           # Text tokenization
├── config/                        # Runtime config (create this)
│   ├── llm_providers.yaml
│   └── ui.yaml
├── tests/                         # Test suite
│   ├── __init__.py
│   ├── test_inference.py
│   ├── test_providers.py
│   └���─ test_routing.py
├── pyproject.toml                 # Package metadata & dependencies
├── README.md                      # This file
├── README_MOBILE.md               # Mobile edition guide
└── LICENSE                        # MIT License
```

---

## Development

### Local Setup

```bash
# Clone and enter repo
git clone https://github.com/fahhede-star/Minimol.git
cd Minimol

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install in editable mode with dev tools
pip install --upgrade pip setuptools wheel
pip install -e .[dev]  # Includes pytest, black, ruff, mypy
```

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_inference.py -v

# Run with coverage
pytest --cov=minimol tests/

# Test routing
python tests/test_routing.py
```

### Code Style

```bash
# Format code
black minimol/

# Lint
ruff check minimol/

# Type checking
mypy minimol/
```

### Adding a New LLM Provider

1. Create `minimol/providers/new_provider_adapter.py`
2. Implement the provider interface (see existing adapters)
3. Register in `minimol/providers/__init__.py`
4. Add config section to `config/llm_providers.yaml`
5. Add tests in `tests/test_providers.py`
6. Update `pyproject.toml` with optional dependency (if needed)

---

## Troubleshooting

### Import Errors After Installation

```bash
# Issue: ModuleNotFoundError or import fails

# Solution 1: Verify venv is active
which python  # Should show path inside .venv

# Solution 2: Reinstall in editable mode
pip install -e .

# Solution 3: Check you're on the correct branch
git branch
git checkout reorg/package-structure
```

### `minimol-ui` Command Not Found

```bash
# Issue: Command not recognized after pip install

# Solution: Reinstall UI extras
pip install -e .[ui]

# Verify console_scripts in pyproject.toml
grep "minimol-ui" pyproject.toml

# Manually run if needed
python -m minimol.terminal_ui
```

### Provider Authentication Failures

```bash
# Issue: "API key not found" or "Invalid credentials"

# Check environment variables are set
echo $OPENAI_API_KEY
echo $ANTHROPIC_API_KEY

# Verify config file enables the provider
cat config/llm_providers.yaml | grep enabled

# Ensure keys are valid (check provider dashboard)
```

### Ollama Connection Refused

```bash
# Issue: "Connection refused" when using local Ollama

# Verify Ollama is running
curl http://localhost:11434/api/tags

# Check config points to correct URL
grep base_url config/llm_providers.yaml

# If using Docker, verify port mapping
docker ps | grep ollama
```

### Slow Inference

```bash
# Use cloud providers with better latency
# Edit config/llm_providers.yaml to select preferred provider
```

---

## Contributing

We welcome contributions! To help:

### Report Issues

- Describe the problem clearly
- Include Python version, OS, and relevant environment info
- Provide error messages and reproducible steps

### Contribute Code

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make changes and add tests
4. Run tests and linting:
   ```bash
   pytest
   black minimol/
   ruff check minimol/
   mypy minimol/
   ```
5. Commit with clear messages
6. Push and create a Pull Request

### Suggested Tasks

- Move example YAMLs into `config/` on the `reorg/package-structure` branch
- Add GitHub Actions CI workflow to run tests automatically
- Contribute new LLM provider adapters
- Improve documentation and examples
- Add more comprehensive tests
- Performance optimizations

---

## License

MIT License — see [LICENSE](LICENSE) for details.

---

## Related Links

- **Mobile Edition:** [README_MOBILE.md](README_MOBILE.md)
- **Issues & Bugs:** [GitHub Issues](https://github.com/fahhede-star/Minimol/issues)
- **Documentation:** [Wiki](https://github.com/fahhede-star/Minimol/wiki)
