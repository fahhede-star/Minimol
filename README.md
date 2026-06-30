# Minimol: Advanced 70B Parameter Neural Network with Terminal UI

A transformer-style neural network and multi-provider LLM router with a Claude-style terminal UI. This repository provides:

- A demo Terminal UI (simulated responses) for interactive exploration.
- An LLM router with adapters for Ollama, Claude, OpenAI, Gemini, and more (config-driven).
- A reference Transformer implementation (Minimol70B) and a trainer (illustrative; default config is very large).

This README updates quickstart and Termux installation steps and clarifies configuration paths and hardware requirements.

---

## Quick start (demo mode — no external LLM required)

This runs the terminal UI demo which simulates responses. Works on low-end machines and Termux.

1. Clone the repo and switch to the reorganization branch:

```bash
git clone https://github.com/fahhede-star/Minimol.git
cd Minimol
git fetch origin
git checkout reorg/package-structure
```

2. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
```

3. Install the package (UI extras):

```bash
pip install --upgrade pip setuptools wheel
pip install -e .[ui]
```

4. Run the terminal UI demo (uses simulated responses):

```bash
minimol-ui
# or
python -m minimol.terminal_ui
```

You should see the interactive terminal UI. This demo does not require any model or cloud API keys.

---

## Running real inference (Ollama / OpenAI / Claude)

The router loads configuration from `config/llm_providers.yaml` by default. The repository contains example YAMLs at the repo root; you can either move them into `config/` or pass the explicit path when creating the InferenceEngine.

Recommended: move the YAMLs into `config/` so the package defaults work:

```bash
mkdir -p config
git mv llm_providers.yaml config/llm_providers.yaml
git mv ui.yaml config/ui.yaml
git commit -m "Move config files into config/ for package defaults"
```

Set environment variables for cloud providers (do not commit keys):

```bash
export OPENAI_API_KEY="sk-..."
export ANTHROPIC_API_KEY="api-..."
```

Example: run the InferenceEngine using OpenAI (once enabled in the YAML):

```bash
python -c "import asyncio; from minimol.inference import InferenceEngine, UseCase; async def r():\
 e = InferenceEngine(); await e.initialize(); print('ready'); await e.cleanup();\
 asyncio.run(r())"
```

Or use the CLI to generate a completion (requires a provider enabled in the YAML and valid keys):

```bash
minimol generate "Explain quantum computing in 2 sentences." --provider openai --model gpt-4
```

Notes:
- Ollama adapter defaults to `http://localhost:11434` and expects an Ollama service running locally.
- If the YAML config references `${ENV_VAR}` for api_key, the loader reads the environment variable.

---

## Termux (Android) installation notes

Termux can run the terminal UI demo but is not suitable for running large local models (PyTorch and 70B model are not feasible on mobile). Use Termux as a client to remote providers instead.

Termux quick steps:

1. Install Termux (F‑Droid recommended), open it and update packages:

```bash
pkg update && pkg upgrade -y
pkg install git python -y
```

2. (Optional build deps) If you need to build wheels:

```bash
pkg install clang make openssl libffi rust -y
```

3. Clone and switch to branch, create venv, install UI dependencies only:

```bash
git clone https://github.com/fahhede-star/Minimol.git
cd Minimol
git fetch origin
git checkout reorg/package-structure
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip setuptools wheel
# If full extras fail, install UI deps individually:
pip install rich prompt-toolkit pygments pyyaml
```

4. Run the terminal UI demo:

```bash
python -m minimol.terminal_ui
```

5. To access remote providers from Termux, set env vars as usual (OPENAI_API_KEY, ANTHROPIC_API_KEY) and ensure your YAML config enables the provider.

Caveats:
- Many ML libraries (torch, transformers, provider SDKs) require native wheels not available on ARM/Termux. Prefer remote APIs or a server for heavy inference.

---

## Hardware & resource notes

- The Python code includes a reference implementation named `Minimol70B`. The default params in the code are illustrative and represent a very large model (~70B). Instantiating the default model will require very large amounts of RAM/GPU memory and will not work on typical consumer hardware.

- For development and testing, create a small/smoke model by overriding constructor params (e.g., small vocab_size, small hidden_dim, few layers). A smoke test example is suggested below.

---

## Suggested smoke test (local)

Create `tests/smoke_small_model.py` and run it to verify imports and a forward pass without heavy memory requirements:

```python
# tests/smoke_small_model.py
from minimol.neural_network import Minimol70B
m = Minimol70B(vocab_size=1000, hidden_dim=128, num_layers=2, num_heads=8, max_seq_length=512, device="cpu")
print('params:', m.param_count)
```

Run with:

```bash
python tests/smoke_small_model.py
```

---

## Configuration

- Default config path used by the code: `config/llm_providers.yaml` and `config/ui.yaml`.
- Example YAMLs are included at the repo root; move them to `config/` as described above.

---

## Troubleshooting

- Import errors after `pip install -e .`: ensure you activated the venv and that the branch `reorg/package-structure` is checked out.
- If `minimol-ui` is not found after installation, re-run `pip install -e .[ui]` and confirm the console-scripts in `pyproject.toml` exist.
- Provider failures: check that the service (Ollama) is running and that API keys are set for cloud providers.

---

## Contributing

If you want, I can also:
- Move the example YAMLs into `config/` on the reorg/package-structure branch and push that update.
- Add a small smoke test file and a GitHub Actions workflow to run it automatically.
- Remove or replace the legacy top-level Python modules to avoid duplication.

If you'd like me to make these changes, reply with which items to apply (e.g., "move-config", "add-test-ci", or "all").

---

License: MIT
