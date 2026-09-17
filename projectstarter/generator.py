from pathlib import Path
import subprocess
import sys


def run_command(command, cwd=None):
    """Run a command."""
    subprocess.run(
        command,
        cwd=cwd,
        check=True
    )


def create_virtual_environment(project_path):
    """Create a virtual environment."""

    venv_path = project_path / ".venv"

    print("Creating virtual environment...")

    run_command(
        [sys.executable, "-m", "venv", ".venv"],
        cwd=project_path
    )

    if sys.platform == "win32":
        return venv_path / "Scripts" / "python.exe"

    return venv_path / "bin" / "python"


def upgrade_pip(python_exe):
    """Upgrade pip."""

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
    """Install a package."""

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
    """Create requirements.txt."""

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
    """Create .gitignore."""

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
        "Activate the virtual environment on Windows:\n\n"
        ".venv\\Scripts\\activate\n\n"
        "Run the application:\n\n"
        "python src/"
        f"{project_name}/main.py\n"
    )

    (project_path / "README.md").write_text(
        readme,
        encoding="utf-8"
    )

    print(
        f"Project '{project_name}' created successfully!"
    )


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
        cwd=project_path
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
        "## Activate virtual environment\n\n"
        "Windows:\n\n"
        ".venv\\Scripts\\activate\n\n"
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
        "## Activate virtual environment\n\n"
        "Windows:\n\n"
        ".venv\\Scripts\\activate\n\n"
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
        "## Activate virtual environment\n\n"
        "Windows:\n\n"
        ".venv\\Scripts\\activate\n\n"
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