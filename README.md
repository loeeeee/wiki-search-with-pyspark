# Wikipedia Search Engine

A Django web application with PySpark async data processing engine for searching Wikipedia articles.

## Project Overview

This project aims to create a high-performance Wikipedia search engine using:
- **Django 5.x** - Web framework
- **PySpark** - Distributed data processing
- **Python 3.13** - Modern Python features

## Project Structure

```
wikipedia-search-engine/
├── config/                     # Django settings directory
│   ├── __init__.py
│   ├── settings.py            # Main Django settings
│   ├── urls.py                # Root URL configuration
│   ├── wsgi.py                # WSGI application
│   └── asgi.py                # ASGI application
├── wikipedia_search_engine/    # Main Django app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
├── templates/                  # HTML templates
│   └── wikipedia_search_engine/
├── static/                     # Static files
├── docs-vibe/                  # Development documentation
├── shell.nix                   # NixOS development environment
├── manage.py                   # Django management script
├── requirements.txt            # Python dependencies
└── README.md
```

## Development Setup

### Prerequisites

- NixOS with nix-shell
- Git

### Quick Start

1. Enter the development environment:
   ```bash
   nix-shell
   ```

2. Run database migrations:
   ```bash
   python manage.py migrate
   ```

3. Start the development server:
   ```bash
   python manage.py runserver
   ```

4. Open your browser at http://127.0.0.1:8000

### Available Endpoints

| Endpoint | Description |
|----------|-------------|
| `/` | Home page with search form |
| `/search/` | Search results page |
| `/health/` | Health check endpoint (JSON) |
| `/admin/` | Django admin interface |

## Development Rules

See `.clinerules/` directory for development guidelines:
- Python 3.13+ required
- Use Python logging with console and file output
- Use Python typing throughout
- Define data structures with dataclass
- Document implementation in `docs-vibe/`

## License

MIT
