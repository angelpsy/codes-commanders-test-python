# Core Application

The `core` folder contains the foundational settings and configurations for the Django project. It includes:

- **Settings**: Configuration files for different environments (e.g., `base.py`, `dev.py`, `prod.py`, `test.py`).
- **URLs**: The root URL configuration for the project.
- **WSGI/ASGI**: Entry points for deploying the application.
- **Views**: Shared or global views that are not tied to specific apps.

## When to Modify

- **Settings**: Update when adding new apps, middleware, or environment-specific configurations.
- **URLs**: Modify when adding or changing global URL patterns.
- **WSGI/ASGI**: Rarely needs changes unless deployment requirements change.
- **Views**: Add or update shared views that are used across multiple apps.

## Best Practices

- Keep environment-specific settings isolated in their respective files (e.g., `dev.py` for development).
- Avoid hardcoding sensitive information; use environment variables instead.
- Test changes to settings and URLs thoroughly to ensure they don't break the application.