# Enterprise API Test Framework

![Logo](https://github.com/pytest-dev/pytest/raw/main/doc/en/img/pytest_logo_curves.svg)

## Overview

Enterprise API Test Framework is a robust, extensible, and pytest-inspired platform for automated API testing. It supports complex test scenarios, plugin architecture, and detailed reporting, making it ideal for enterprise-grade projects.

## Architecture

- **Modular Design:**
  - `src/` contains core utilities (random data, loaders, API helpers, config, logging, email, JWT, etc.)
  - `tests/` contains unit and integration tests for each utility
  - Config files (YAML, JSON) for flexible setup
- **Plugin System:**
  - Easily extend with custom plugins
  - Auto-discovery and hooks for integration
- **Fixtures & Parametrization:**
  - Support for reusable fixtures and test parameterization
- **Reporting:**
  - JUnitXML, code coverage, colored terminal output, and summary features

## Testing

- Built on pytest principles: simple `assert` statements, auto-discovery, modular fixtures
- Example test:

```python
from src.random_user import random_user_profile

def test_random_user():
    user = random_user_profile()
    assert 'email' in user
    assert user['age'] > 0
```

- Run all tests:

```bash
pytest
```

- Coverage:

```bash
pytest --cov=src
```

## Getting Started

1. Clone the repo
2. Create a virtual environment and install dependencies
3. Run tests and explore features

## Inspiration

This project is inspired by [pytest](https://github.com/pytest-dev/pytest), leveraging its best practices for test discovery, fixtures, plugins, and reporting.

## License

MIT License. See LICENSE for details.
