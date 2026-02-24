# Wikipedia Search Engine

A Django web application with PySpark async data processing engine for searching Wikipedia articles.

## Project Structure

```
wikipedia-search-engine/
├── config/                 # Django project configuration
│   ├── settings.py         # Django settings
│   ├── urls.py             # Root URL configuration
│   ├── asgi.py             # ASGI application
│   └── wsgi.py             # WSGI application
├── core/                   # Django app for core functionality
│   ├── views.py            # View functions
│   ├── urls.py             # App URL configuration
│   └── ...
├── manage.py               # Django management script
├── pyproject.toml          # Project dependencies
└── docs-vibe/              # Documentation
```

## Quick Start

1. Run migrations:
   ```
   uv run python manage.py migrate
   ```

2. Start the development server:
   ```
   uv run python manage.py runserver
   ```

3. Access the application at `http://localhost:8000/`

## Development

- Python 3.13+
- Django 6.0.2+
- Uses `uv` for dependency management
- Uses `django-admin` for project management

