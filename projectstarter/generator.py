from pathlib import Path
import subprocess
import sys


# ==============================
# Utility Functions
# ==============================

def run_command(command, cwd=None):
    """Run a shell command safely."""

    return subprocess.run(
        command,
        cwd=cwd,
        check=True
    )


def create_virtual_environment(project_path):
    """Create a cross-platform virtual environment."""

    project_path = Path(project_path).resolve()
    venv_path = project_path / ".venv"

    print("Creating virtual environment...")

    run_command(
        [sys.executable, "-m", "venv", ".venv"],
        cwd=project_path
    )

    if sys.platform == "win32":
        python_exe = venv_path / "Scripts" / "python.exe"
    else:
        python_exe = venv_path / "bin" / "python"

    # Return an absolute path to avoid cwd-related issues.
    python_exe = python_exe.resolve()

    if not python_exe.exists():
        raise FileNotFoundError(
            f"Virtual environment Python not found: {python_exe}"
        )

    return python_exe


def upgrade_pip(python_exe):
    """Upgrade pip inside the virtual environment."""

    print("Upgrading pip...")

    run_command(
        [
            str(python_exe),
            "-m",
            "pip",
            "install",
            "--upgrade",
            "pip"
        ]
    )


def install_package(python_exe, package):
    """Install a package inside the virtual environment."""

    print(f"Installing {package}...")

    run_command(
        [
            str(python_exe),
            "-m",
            "pip",
            "install",
            package
        ]
    )


def save_requirements(python_exe, project_path):
    """Generate requirements.txt using pip freeze."""

    project_path = Path(project_path).resolve()

    result = subprocess.run(
        [
            str(python_exe),
            "-m",
            "pip",
            "freeze"
        ],
        capture_output=True,
        text=True,
        check=True
    )

    (project_path / "requirements.txt").write_text(
        result.stdout,
        encoding="utf-8"
    )


def create_gitignore(project_path, django=False):
    """Create a .gitignore file."""

    content = """__pycache__/
*.py[cod]

.venv/
venv/

.env

.pytest_cache/
.vscode/
"""

    if django:
        content += "\ndb.sqlite3\n"

    (project_path / ".gitignore").write_text(
        content,
        encoding="utf-8"
    )


def activation_instructions():
    """Return cross-platform virtual environment instructions."""

    return """## Activate virtual environment

Windows:

.venv\\Scripts\\activate

Linux / macOS:

source .venv/bin/activate

"""


# ==============================
# Python Project Generator
# ==============================

def create_python_project(project_name):
    """Create a basic Python project."""

    project_path = Path(project_name)

    if project_path.exists():
        raise FileExistsError(
            f"Project '{project_name}' already exists."
        )

    print(f"Creating Python project '{project_name}'...")

    package_path = project_path / "src" / project_name
    tests_path = project_path / "tests"

    package_path.mkdir(parents=True)
    tests_path.mkdir(parents=True)

    (package_path / "__init__.py").write_text(
        "",
        encoding="utf-8"
    )

    (package_path / "main.py").write_text(
        """def main():
    print("Hello from your new Python project!")


if __name__ == "__main__":
    main()
""",
        encoding="utf-8"
    )

    (tests_path / "test_main.py").write_text(
        """def test_example():
    assert True
""",
        encoding="utf-8"
    )

    create_gitignore(project_path)

    (project_path / "requirements.txt").write_text(
        "",
        encoding="utf-8"
    )

    readme = (
        f"# {project_name}\n\n"
        "A Python project created with ProjectStarter.\n\n"
        "## Run\n\n"
        "Run the application:\n\n"
        f"python src/{project_name}/main.py\n"
    )

    (project_path / "README.md").write_text(
        readme,
        encoding="utf-8"
    )

    print(
        f"Project '{project_name}' created successfully!"
    )


# ==============================
# Django Project Generator
# ==============================

def create_django_project(project_name):
    """Create a Django project."""

    project_path = Path(project_name)

    if project_path.exists():
        raise FileExistsError(
            f"Project '{project_name}' already exists."
        )

    print(f"Creating Django project '{project_name}'...")

    project_path.mkdir(parents=True)

    python_exe = create_virtual_environment(
        project_path
    )

    upgrade_pip(python_exe)

    install_package(
        python_exe,
        "django"
    )

    print("Creating Django project files...")

    run_command(
        [
            str(python_exe),
            "-m",
            "django",
            "startproject",
            "config",
            "."
        ],
        cwd=project_path.resolve()
    )

    save_requirements(
        python_exe,
        project_path
    )

    create_gitignore(
        project_path,
        django=True
    )

    readme = (
        f"# {project_name}\n\n"
        "A Django project created with ProjectStarter.\n\n"
        f"{activation_instructions()}"
        "## Run the project\n\n"
        "python manage.py runserver\n\n"
        "## Project URL\n\n"
        "http://127.0.0.1:8000/\n"
    )

    (project_path / "README.md").write_text(
        readme,
        encoding="utf-8"
    )

    print(
        f"Django project '{project_name}' "
        "created successfully!"
    )


# ==============================
# Flask Project Generator
# ==============================

def create_flask_project(project_name):
    """Create a Flask project."""

    project_path = Path(project_name)

    if project_path.exists():
        raise FileExistsError(
            f"Project '{project_name}' already exists."
        )

    print(f"Creating Flask project '{project_name}'...")

    project_path.mkdir(parents=True)

    python_exe = create_virtual_environment(
        project_path
    )

    upgrade_pip(python_exe)

    install_package(
        python_exe,
        "flask"
    )

    app_path = project_path / "app"
    templates_path = app_path / "templates"
    static_path = app_path / "static"

    templates_path.mkdir(parents=True)
    static_path.mkdir(parents=True)

    (app_path / "__init__.py").write_text(
        """from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Hello from Flask!"

    return app
""",
        encoding="utf-8"
    )

    (project_path / "run.py").write_text(
        """from app import create_app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
""",
        encoding="utf-8"
    )

    save_requirements(
        python_exe,
        project_path
    )

    create_gitignore(
        project_path
    )

    readme = (
        f"# {project_name}\n\n"
        "A Flask project created with ProjectStarter.\n\n"
        f"{activation_instructions()}"
        "## Run the project\n\n"
        "python run.py\n\n"
        "## Project URL\n\n"
        "http://127.0.0.1:5000/\n"
    )

    (project_path / "README.md").write_text(
        readme,
        encoding="utf-8"
    )

    print(
        f"Flask project '{project_name}' "
        "created successfully!"
    )


# ==============================
# FastAPI Project Generator
# ==============================

def create_fastapi_project(project_name):
    """Create a FastAPI project."""

    project_path = Path(project_name)

    if project_path.exists():
        raise FileExistsError(
            f"Project '{project_name}' already exists."
        )

    print(f"Creating FastAPI project '{project_name}'...")

    project_path.mkdir(parents=True)

    python_exe = create_virtual_environment(
        project_path
    )

    upgrade_pip(python_exe)

    install_package(
        python_exe,
        "fastapi"
    )

    install_package(
        python_exe,
        "uvicorn"
    )

    app_path = project_path / "app"
    app_path.mkdir(parents=True)

    (app_path / "__init__.py").write_text(
        "",
        encoding="utf-8"
    )

    (app_path / "main.py").write_text(
        """from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello from FastAPI!"}
""",
        encoding="utf-8"
    )

    save_requirements(
        python_exe,
        project_path
    )

    create_gitignore(
        project_path
    )

    readme = (
        f"# {project_name}\n\n"
        "A FastAPI project created with ProjectStarter.\n\n"
        f"{activation_instructions()}"
        "## Run\n\n"
        "uvicorn app.main:app --reload\n\n"
        "## API\n\n"
        "http://127.0.0.1:8000/\n\n"
        "## Swagger Docs\n\n"
        "http://127.0.0.1:8000/docs\n"
    )

    (project_path / "README.md").write_text(
        readme,
        encoding="utf-8"
    )

    print(
        f"FastAPI project '{project_name}' "
        "created successfully!"
    )