# nginx-configurator

[![CI](https://img.shields.io/github/actions/workflow/status/user/nginx-configurator/ci.yml?branch=main)]()
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)]()
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

> Nginx configuration generator with load balancing and SSL templates

A Python project focused on solving real-world engineering problems.

## Features

- **Comprehensive Logging** — Structured logging with configurable log levels
- **Async Support** — Native asyncio integration with sync fallback
- **Rich CLI** — Interactive CLI with colored output and progress bars
- **Minimal Dependencies** — Only standard library dependencies for core features

## Installation

```bash
pip install nginx-configurator
# or
pipx install nginx-configurator
```

## Usage

```python
from nginx_configurator import Client

client = Client(
    timeout=30,
    retries=3,
)

result = client.run()
print(result)
```

## Configuration

Configuration can be provided via environment variables, a config file, or programmatically.

| Variable | Description | Default |
|----------|-------------|--------|
| `NGINX_CONFIGURATOR_TIMEOUT` | Request timeout in seconds | `30` |
| `NGINX_CONFIGURATOR_RETRIES` | Number of retry attempts | `3` |
| `NGINX_CONFIGURATOR_LOG_LEVEL` | Log verbosity (debug, info, warn, error) | `info` |

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
