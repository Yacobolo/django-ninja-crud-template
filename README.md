# Django Ninja Crud Template

This is a robust Django project template that provides a seamless implementation of `django-ninja`, `django-ninja-jwt`, and `django-ninja-crud`. It's crafted to jump-start your Django project, ensuring a solid and efficient foundation with JWT authentication, CRUD operations, and more, all built on the powerful Django Ninja framework.

## Features

- 🛡️ **JWT Authentication** (using `django-ninja-jwt`): Securely manage user authentication with JSON Web Tokens.
- 📝 **CRUD Operations** (using `django-ninja-crud`): Easily perform Create, Read, Update, and Delete operations.
- 🗑️ **Soft Delete**: Safely delete objects without losing the data, allowing for recovery.
- 🕰️ **Simple History**: Keep track of changes to models with historical records.
- 🏷️ **Metadata Fields**: Automatically manage metadata fields like `created_at`, `updated_at`, `created_by`, `updated_by`, and `deleted_at`.
- 🥋 **Built on Django Ninja** (`django-ninja`): Enjoy the simplicity and speed of building APIs with Django Ninja.

## Repository Structure

```plaintext
django-ninja-crud-template/
│
├── backend/              # Backend codebase
│   ├── api/              # API app containing the main functionality
│   │   ├── models/       # --> Contains the database model definitions
│   │   ├── schemas/      # --> Houses the Pydantic schemas for API serialization
│   │   ├── services/     # --> Contains business logic separate from models and views
│   │   ├── utils/        # --> Utility functions and classes
│   │   ├── views/        # --> View functions and handlers for API requests
│   │   └── api.py        # --> Main file for API route definitions
│   ├── manage.py         # --> Django management script
│   └── yourproject/      # Main project configuration
│       ├── settings.py   # --> Project settings and configuration
│       ├── urls.py       # --> URL configuration for the project
│       └── wsgi.py       # --> WSGI configuration for deployment
│
├── frontend/             # Frontend codebase (if applicable)
```
