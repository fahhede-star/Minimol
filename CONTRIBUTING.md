# Contributing to Minimol

Thank you for your interest in contributing to Minimol! This guide will help you set up a development environment and understand how to contribute effectively.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Project Structure](#project-structure)
- [How to Contribute](#how-to-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Proposing Features](#proposing-features)
  - [Submitting Code](#submitting-code)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Common Tasks](#common-tasks)

---

## Code of Conduct

Be respectful, inclusive, and professional. We're building this together.

---

## Getting Started

### Prerequisites

- **Python:** 3.10 or higher
- **Git:** For version control
- **pip:** For package management
- **Virtual environment:** Recommended (venv or conda)

### Quick Setup

```bash
# Clone the repository
git clone https://github.com/fahhede-star/Minimol.git
cd Minimol

# Check out the development branch
git checkout reorg/package-structure

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Upgrade core tools
pip install --upgrade pip setuptools wheel

# Install with dev dependencies
pip install -e .[dev]
```

---

## Development Setup

### Install Development Dependencies

```bash
pip install -e .[dev]
# Includes: pytest, pytest-asyncio, pytest-cov, black, ruff, mypy
```

### Verify Installation

```bash
# Run smoke test
python tests/smoke_small_model.py

# Run full test suite
pytest

# Check code style
black --check minimol/
ruff check minimol/

# Type checking
mypy minimol/
```

---

## Project Structure

### Main Package (`minimol/`)

```
minimol/
├── __init__.py              # Package initialization
├── terminal_ui.py           # Claude-style interactive UI
├── inference.py             # LLM router & InferenceEngine (core logic)
├── neural_network.py        # Minimol70B transformer (reference model)
├── trainer.py               # Training loop (illustrative)
├── cli.py                   # Command-line interface entry points
├── providers/               # LLM provider adapters
│   ├── __init__.py
│   ├── base_adapter.py      # Abstract provider interface
│   ├── openai_adapter.py    # OpenAI integration
│   ├── anthropic_adapter.py # Claude integration
│   ├── ollama_adapter.py    # Ollama local inference
│   ├── gemini_adapter.py    # Google Gemini
│   ├── mistral_adapter.py   # Mistral
│   └── cohere_adapter.py    # Cohere
├── config/                  # Configuration loaders
│   ├── __init__.py
│   └── loader.py            # YAML config parsing & env var injection
└── utils/                   # Utility functions
    ├── __init__.py
    └── tokenizer.py         # Text tokenization
```

### Key Classes & Interfaces

#### `minimol/providers/base_adapter.py`

```python
class ProviderAdapter(ABC):
    """Abstract base for all LLM provider integrations."""
    
    @abstractmethod
    async def initialize(self):
        """Setup provider connection."""
        pass
    
    @abstractmethod
    async def generate(self, prompt: str, **kwargs) -> str:
        """Generate response from prompt."""
        pass
    
    @abstractmethod
    async def cleanup(self):
        """Cleanup resources."""
        pass
```

#### `minimol/inference.py`

```python
class InferenceEngine:
    """Multi-provider LLM router."""
    
    async def initialize(self):
        """Load config and initialize providers."""
    
    async def generate(self, prompt: str, provider: str, **kwargs) -> str:
        """Route request to selected provider."""
    
    async def cleanup(self):
        """Cleanup all providers."""
```

### Tests (`tests/`)

```
tests/
├── __init__.py
├── test_inference.py        # InferenceEngine tests
├── test_providers.py        # Provider adapter tests
├── test_config.py           # Configuration loading tests
└── smoke_small_model.py     # Lightweight model verification
```

---

## How to Contribute

### Reporting Bugs

**Before reporting, check if the issue already exists:**

1. Search [GitHub Issues](https://github.com/fahhede-star/Minimol/issues)
2. Check [Troubleshooting](README.md#troubleshooting) section in README

**When reporting, include:**

```markdown
**Title:** Brief description of bug

**Environment:**
- Python version: `python --version`
- OS: macOS / Linux / Windows
- Installation method: `pip install -e .[ui]` or `[mobile]`
- Branch: `git branch`

**Steps to Reproduce:**
1. ...
2. ...
3. ...

**Expected Behavior:**
What should happen?

**Actual Behavior:**
What actually happens?

**Error Message/Logs:**
```
Full traceback or logs here
```

**Additional Context:**
Any other relevant info (config, environment variables, etc.)
```

### Proposing Features

**Before proposing, check if similar features exist:**

1. Search [GitHub Issues](https://github.com/fahhede-star/Minimol/issues)
2. Review [README.md](README.md) for existing capabilities

**When proposing, include:**

```markdown
**Title:** Brief feature description

**Problem It Solves:**
What pain point does this address?

**Proposed Solution:**
How should it work?

**Example Usage:**
```python
# Show how users would use this feature
minimol generate("...", new_feature=True)
```

**Alternatives Considered:**
Other approaches you've thought about

**Additional Context:**
Why this matters, use cases, etc.
```

### Submitting Code

#### Step 1: Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b bugfix/issue-description
```

**Branch naming:**
- `feature/` for new features
- `bugfix/` for bug fixes
- `docs/` for documentation
- `refactor/` for code refactoring
- `chore/` for maintenance tasks

#### Step 2: Make Your Changes

```bash
# Edit files
vim minimol/your_module.py

# Test frequently
pytest tests/

# Format code
black minimol/

# Lint
ruff check minimol/ --fix

# Type check
mypy minimol/
```

#### Step 3: Write/Update Tests

All new code should have tests. Aim for >80% coverage.

```bash
# Run tests with coverage
pytest --cov=minimol tests/

# Check coverage report
coverage report
```

#### Step 4: Commit with Clear Messages

```bash
git add minimol/your_module.py tests/test_your_module.py
git commit -m "feat: add new LLM provider support

- Implement XyzAdapter class
- Add configuration support in llm_providers.yaml
- Add tests for new provider
- Update README with setup instructions

Fixes #123"
```

**Commit message format:**
```
<type>: <short description (50 chars max)>

<optional detailed explanation (72 char wrapping)>

Fixes #<issue_number>
Refs #<related_issues>
```

**Types:** `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `perf`

#### Step 5: Push and Create a Pull Request

```bash
git push origin feature/your-feature-name
```

**Then open a PR on GitHub with:**

```markdown
## Description
Brief summary of changes

## Related Issues
Fixes #123
Related to #456

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation
- [ ] Refactoring

## Testing
- [ ] Unit tests added/updated
- [ ] Manual testing completed
- [ ] All tests pass

## Checklist
- [ ] Code follows style guidelines (black, ruff)
- [ ] Type hints added (mypy passes)
- [ ] Documentation updated
- [ ] No new warnings generated
```

---

## Coding Standards

### Style Guide

We use **Black** and **Ruff** for formatting and linting.

```bash
# Auto-format all code
black minimol/

# Fix linting issues
ruff check minimol/ --fix

# Type checking
mypy minimol/
```

### Python Style

- **Line length:** 100 characters (Black default)
- **Imports:** Organized (stdlib, third-party, local)
- **Naming:**
  - `snake_case` for functions and variables
  - `PascalCase` for classes
  - `UPPER_CASE` for constants
- **Type hints:** Required for all functions
  ```python
  async def generate(self, prompt: str, **kwargs) -> str:
      """Generate response."""
  ```
- **Docstrings:** Google-style format
  ```python
  def method(param: str) -> bool:
      """Short description.
      
      Longer description if needed.
      
      Args:
          param: Description of param.
      
      Returns:
          Description of return value.
      
      Raises:
          ValueError: When param is invalid.
      """
  ```

### Async-First

Minimol uses async/await throughout. Always use `async def` for I/O operations:

```python
# ✅ Good
async def initialize(self):
    await self.client.connect()

# ❌ Avoid
def initialize(self):
    asyncio.run(self.client.connect())
```

---

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run specific file
pytest tests/test_inference.py -v

# Run specific test
pytest tests/test_inference.py::test_initialize -v

# Run with coverage
pytest --cov=minimol tests/

# Run smoke test (lightweight)
python tests/smoke_small_model.py
```

### Writing Tests

```python
# tests/test_new_feature.py
import pytest
from minimol.new_module import new_function

@pytest.mark.asyncio
async def test_new_function():
    """Test new_function behavior."""
    result = await new_function("input")
    assert result == "expected_output"

@pytest.mark.asyncio
async def test_new_function_error():
    """Test new_function error handling."""
    with pytest.raises(ValueError):
        await new_function("invalid")
```

### Test Structure

- **Unit tests:** Test single functions/methods in isolation
- **Integration tests:** Test multiple components together
- **Smoke tests:** Quick sanity checks (no heavy computation)
- **Fixtures:** Reusable test setup (see `conftest.py`)

---

## Common Tasks

### Adding a New LLM Provider

1. **Create adapter file:**
   ```bash
   touch minimol/providers/myservice_adapter.py
   ```

2. **Implement ProviderAdapter:**
   ```python
   from minimol.providers.base_adapter import ProviderAdapter
   
   class MyServiceAdapter(ProviderAdapter):
       async def initialize(self):
           # Setup connection
           pass
       
       async def generate(self, prompt: str, **kwargs) -> str:
           # Call API and return response
           pass
       
       async def cleanup(self):
           # Cleanup resources
           pass
   ```

3. **Register in `minimol/providers/__init__.py`:**
   ```python
   from .myservice_adapter import MyServiceAdapter
   
   __all__ = ["MyServiceAdapter", ...]
   ```

4. **Update `pyproject.toml`:**
   ```toml
   [project.optional-dependencies]
   myservice = ["myservice-sdk>=1.0.0"]
   ```

5. **Add tests:**
   ```python
   # tests/test_providers.py
   @pytest.mark.asyncio
   async def test_myservice_adapter():
       adapter = MyServiceAdapter()
       await adapter.initialize()
       result = await adapter.generate("hello")
       assert len(result) > 0
   ```

6. **Update README.md** with setup instructions

7. **Commit:**
   ```bash
   git commit -m "feat: add MyService LLM provider support"
   ```

### Updating Documentation

```bash
# Edit README.md, CONTRIBUTING.md, or README_MOBILE.md
vim README.md

# Format and commit
git add README.md
git commit -m "docs: improve provider setup instructions"
```

### Fixing a Bug

```bash
# Create bugfix branch
git checkout -b bugfix/fix-provider-timeout

# Make fix with tests
# ... edit minimol/providers/base_adapter.py
# ... edit tests/test_providers.py

# Run tests to verify
pytest tests/test_providers.py -v

# Commit with reference to issue
git commit -m "fix: handle provider timeout correctly

Fixes #456
- Add 30s timeout to provider calls
- Retry failed requests once
- Log timeout errors clearly"
```

### Running the Full Development Workflow

```bash
# Create branch
git checkout -b feature/awesome-feature

# Make changes and test frequently
pytest
black minimol/ && ruff check minimol/ --fix && mypy minimol/

# Before pushing, run final checks
pytest --cov=minimol tests/
coverage report

# Push and create PR
git push origin feature/awesome-feature
```

---

## Questions?

- **Issues:** [GitHub Issues](https://github.com/fahhede-star/Minimol/issues)
- **Discussions:** [GitHub Discussions](https://github.com/fahhede-star/Minimol/discussions)
- **Code Review:** We'll review all PRs thoroughly

---

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

Happy coding! 🚀
