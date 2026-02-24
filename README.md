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

## Environment Variables

Environment variables are stored in `env.yaml` and automatically loaded when entering the nix shell.

### Default Variables

The following variables are created automatically if `env.yaml` does not exist:

- `DEBUG`: Set to `false` by default
- `SECRET_KEY`: Development key (change in production)
- `DATABASE_URL`: SQLite database path
- `LOG_LEVEL`: Set to `INFO`
- `PYTHON_ENV`: Set to `development`

### Modifying Environment Variables

Edit `env.yaml` to customize environment variables, then re-enter the nix shell to reload them.

