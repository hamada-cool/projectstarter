from .generator import (
    create_python_project,
    create_django_project,
    create_flask_project,
    create_fastapi_project,
)

GENERATORS = {
"python": create_python_project,
"django": create_django_project,
"flask": create_flask_project,
"fastapi": create_fastapi_project,
}

PROJECT_INFO = {
    "python": {
        "description": "A basic Python project",
        "virtual_environment": "Yes",
        "automatic_installation": "No",
        "run": "python src/<project_name>/main.py",
    },

    "django": {
        "description": "Python web framework",
        "virtual_environment": "Yes",
        "automatic_installation": "Yes",
        "run": "python manage.py runserver",
    },

    "flask": {
        "description": "Lightweight Python web framework",
        "virtual_environment": "Yes",
        "automatic_installation": "Yes",
        "run": "python run.py",
    },

    "fastapi": {
        "description": "Modern Python API framework",
        "virtual_environment": "Yes",
        "automatic_installation": "Yes",
        "run": "uvicorn app.main:app --reload",
    },
}