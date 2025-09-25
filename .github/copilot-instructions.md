# Copilot Instructions for AI Coding Agents

## Project Overview
This is a Django-based web application with a modular structure. The main components are:
- `hmd/`: Project settings, URLs, and WSGI/ASGI entry points.
- `core/`, `analytics/`, `pages/`: Django apps containing models, views, admin, migrations, and tests.
- `media/`: User-uploaded files and images, organized by feature (e.g., portfolio, slider).
- `static/`: Static assets (CSS, JS, images).
- `templates/`: HTML templates for pages and admin views.

## Architecture & Data Flow
- Each app (`core`, `analytics`, `pages`) encapsulates related models, views, and admin logic.
- Data flows from models (in `models.py`) to views (in `views.py`), rendered via templates in `templates/`.
- Static and media files are served separately; media is for uploads, static for assets.
- Migrations are managed per app in `migrations/`.

## Developer Workflows
- **Run server:** `python manage.py runserver`
- **Apply migrations:** `python manage.py migrate`
- **Create migrations:** `python manage.py makemigrations <appname>`
- **Run tests:** `python manage.py test <appname>`
- **Debug:** Use Django's built-in error pages and logging in `settings.py`.

## Project-Specific Conventions
- Apps follow Django's standard structure, but some logic (e.g., Facebook API integration) is in `core/facebook_api.py`.
- Custom admin extensions are in `hmd/admin_extra.py`.
- Context processors are defined in `core/context_processors.py` for injecting global template variables.
- Templates are organized by feature and admin section (e.g., `templates/admin/`, `templates/pages/`).
- Media files are grouped by feature for easier management.

## Integration Points & Dependencies
- External integrations (e.g., Facebook API) are handled in dedicated modules (`core/facebook_api.py`).
- Database is SQLite (`db.sqlite3`), but can be swapped via Django settings.
- No `.env` file detected; secrets and config are likely in `hmd/settings.py`.

## Patterns & Examples
- **Model-View-Template:**
  - Example: `core/models.py`, `core/views.py`, `templates/index.html`
- **Custom Admin:**
  - Example: `hmd/admin_extra.py`
- **Context Processors:**
  - Example: `core/context_processors.py`
- **Migrations:**
  - Example: `core/migrations/0001_initial.py`

## Key Files & Directories
- `manage.py`: Main entry for Django commands
- `hmd/settings.py`: Project settings
- `core/`, `analytics/`, `pages/`: Main Django apps
- `media/`, `static/`, `templates/`: Assets and templates

## AI Agent Guidance
- Prefer Django management commands for all workflows.
- When editing models, always create and apply migrations.
- Follow app/module boundaries; avoid cross-app imports unless necessary.
- Use context processors for global template data.
- Place new templates in the appropriate feature or admin subdirectory.
- For external API logic, use or extend dedicated modules (e.g., `facebook_api.py`).

---
For questions or unclear conventions, ask for clarification or examples from the user.
