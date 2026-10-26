# projectstarter-cli 🚀

[![PyPI version](https://img.shields.io/pypi/v/projectstarter-cli)](https://pypi.org/project/projectstarter-cli/)
[![Python Versions](https://img.shields.io/pypi/pyversions/projectstarter-cli)](https://pypi.org/project/projectstarter-cli/)
[![Tests](https://github.com/hamada-cool/projectstarter/actions/workflows/python-tests.yml/badge.svg)](https://github.com/hamada-cool/projectstarter/actions/workflows/python-tests.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/hamada-cool/projectstarter/blob/main/LICENSE)

**Create ready-to-use Python projects in seconds.**

`projectstarter-cli` is a Python command-line tool created by **Mohamed Ali Ismail Jami** to simplify project setup. It automatically generates project structures and, for supported web frameworks, creates virtual environments and installs the required dependencies.

Spend less time configuring projects and more time building applications.

## ✨ Features

- 🐍 Generate basic Python projects.
- 🌐 Generate Django projects.
- ⚡ Generate Flask projects.
- 🚀 Generate FastAPI projects.
- 📦 Automatically create `.venv` for Django, Flask, and FastAPI projects.
- ⬆️ Automatically upgrade `pip` in generated framework environments.
- 🔧 Install the required framework dependencies.
- 📄 Generate `requirements.txt`.
- 🚫 Generate `.gitignore`.
- 📝 Generate a project-specific `README.md`.
- 📋 List supported project types.
- ℹ️ Display information about each generator.
- 🩺 Diagnose the installation using the `doctor` command.
- 🧪 Run automated tests with `pytest`.

## 📋 Supported Project Types

| Project Type | Virtual Environment | Automatic Dependency Installation | Run Command |
|---|---|---|---|
| Python | No | No | `python src/<project_name>/main.py` |
| Django | Yes | Yes | `python manage.py runserver` |
| Flask | Yes | Yes | `python run.py` |
| FastAPI | Yes | Yes | `uvicorn app.main:app --reload` |

> **Note:** The basic Python generator creates the project structure directly. Django, Flask, and FastAPI generators create their own virtual environments and install their framework dependencies.

## 📦 Installation

Install `projectstarter-cli` from PyPI:

```bash
python -m pip install projectstarter-cli
```

Verify the installation:

```bash
projectstarter --version
```

Display the available commands:

```bash
projectstarter --help
```

## 🚀 Usage

### 1. Create a Project Interactively

Run:

```bash
projectstarter create
```

Choose a project type when prompted:

```text
Choose a project type:

1. python
2. django
3. flask
4. fastapi
```

Enter your choice and project name:

```text
Enter your choice: 2
Enter project name: myproject
```

The CLI generates the selected project automatically.

### 2. Create a Python Project

Generate a basic Python project:

```bash
projectstarter create python myproject
```

#### Generated Structure

```text
myproject/
├── src/
│   └── myproject/
│       ├── __init__.py
│       └── main.py
├── tests/
│   └── test_main.py
├── .gitignore
├── requirements.txt
└── README.md
```

#### Run the Project

On Windows, macOS, or Linux:

```bash
python src/myproject/main.py
```

The generated application includes a simple `main()` function.

## 🌐 Django

Create a Django project:

```bash
projectstarter create django myproject
```

The generator automatically:

1. Creates the project directory.
2. Creates a `.venv` virtual environment.
3. Upgrades `pip`.
4. Installs Django.
5. Creates the Django project using the `config` package.
6. Generates `requirements.txt`.
7. Generates `.gitignore`.
8. Generates a project-specific README.

### Generated Structure

```text
myproject/
├── .venv/
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

### Activate the Virtual Environment

**Windows (Command Prompt):**

```bat
cd myproject
.venv\Scripts\activate
```

**Windows (PowerShell):**

```powershell
cd myproject
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
cd myproject
source .venv/bin/activate
```

### Run Django

```bash
python manage.py runserver
```

Open the development server:

http://127.0.0.1:8000/

## ⚡ Flask

Create a Flask project:

```bash
projectstarter create flask myproject
```

The generator automatically:

1. Creates the project directory and `.venv`.
2. Upgrades `pip`.
3. Installs Flask.
4. Creates the `app` package.
5. Creates the `templates/` and `static/` directories.
6. Creates `run.py`.
7. Generates `requirements.txt`.
8. Generates `.gitignore` and a project README.

### Generated Structure

```text
myproject/
├── .venv/
├── app/
│   ├── __init__.py
│   ├── templates/
│   └── static/
├── run.py
├── requirements.txt
├── .gitignore
└── README.md
```

### Activate the Virtual Environment

**Windows:**

```bat
cd myproject
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
cd myproject
source .venv/bin/activate
```

### Run Flask

```bash
python run.py
```

Open the development server:

http://127.0.0.1:5000/

## 🚀 FastAPI

Create a FastAPI project:

```bash
projectstarter create fastapi myproject
```

The generator automatically:

1. Creates the project directory and `.venv`.
2. Upgrades `pip`.
3. Installs FastAPI.
4. Installs Uvicorn.
5. Creates the `app` package.
6. Creates `app/main.py` and `app/__init__.py`.
7. Generates `requirements.txt`.
8. Generates `.gitignore` and a project README.

### Generated Structure

```text
myproject/
├── .venv/
├── app/
│   ├── __init__.py
│   └── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

### Activate the Virtual Environment

**Windows:**

```bat
cd myproject
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
cd myproject
source .venv/bin/activate
```

### Run FastAPI

```bash
uvicorn app.main:app --reload
```

Open the API:

http://127.0.0.1:8000/

Explore the interactive API documentation:

http://127.0.0.1:8000/docs

## 📋 List Project Types

Display all supported project generators:

```bash
projectstarter list
```

Example output:

```text
Available project types:

python
django
flask
fastapi
```

## ℹ️ Project Information

Use the `info` command to learn about a generator:

```bash
projectstarter info django
```

Example output:

```text
Django
──────────────────────────────
Description: Python web framework
Virtual environment: Yes
Automatic installation: Yes

Run:
    python manage.py runserver
```

Get information about other generators:

```bash
projectstarter info python
projectstarter info flask
projectstarter info fastapi
```

## 🩺 Doctor

Use the built-in diagnostic command to check your installation:

```bash
projectstarter doctor
```

The diagnostic checks:

- Python availability and version.
- Project generator registry.
- Available generators.
- Project information for supported generators.

Example output:

```text
projectstarter-cli Doctor
──────────────────────────────
✓ Python
  Version: 3.x.x
✓ Registry
✓ Generators (4)
  - python
  - django
  - flask
  - fastapi
✓ Project Info
  All project information is available.

Everything looks good! ✓
```

*Actual output may vary depending on your Python version and installation.*

## 🧪 Testing

`projectstarter-cli` uses `pytest` for automated testing.

### Install pytest

```bash
python -m pip install pytest
```

### Run the Tests

From the repository root:

```bash
python -m pytest
```

The test suite covers:

- Project name validation.
- Generator registry.
- Project information.
- Python project generation.
- Django project generation.
- Flask project generation.
- FastAPI project generation.
- CLI commands.
- Interactive project creation.
- Doctor diagnostics.

### Continuous Integration

GitHub Actions runs the automated tests against Python 3.13 and 3.14.

[View the GitHub Actions workflow](https://github.com/hamada-cool/projectstarter/actions/workflows/python-tests.yml)

## 🏗️ Development Structure

The repository is organized as follows:

```text
projectstarter/
├── .github/
│   └── workflows/
│       └── python-tests.yml
├── projectstarter/
│   ├── __init__.py
│   ├── cli.py
│   ├── doctor.py
│   ├── generator.py
│   ├── registry.py
│   └── utils.py
├── templates/
│   └── python/
│       └── main.py
├── tests/
│   ├── test_cli.py
│   ├── test_generator.py
│   ├── test_registry.py
│   └── test_utils.py
├── README.md
├── LICENSE
└── pyproject.toml
```

### Main Components

| File | Responsibility |
|---|---|
| `cli.py` | Implements CLI commands such as `create`, `list`, `info`, `doctor`, and `--version`. |
| `generator.py` | Implements project generation, virtual environment creation, and dependency installation. |
| `registry.py` | Registers project generators and stores project information. |
| `utils.py` | Provides utility functions, including project-name validation. |
| `doctor.py` | Implements installation diagnostics. |
| `templates/` | Stores project templates. |
| `tests/` | Contains the automated test suite. |

## ➕ Adding a New Generator

The project is designed to support additional generators.

To add a new project type:

1. Implement its generation logic in `generator.py`.
2. Register the generator in `registry.py`.
3. Add its metadata to `PROJECT_INFO`.
4. Add generator tests in `tests/test_generator.py`.
5. Add CLI tests where necessary.
6. Update the documentation in `README.md`.

Keep the implementation, registry, project information, tests, and documentation synchronized.

## 🔐 Project Name Rules

`projectstarter-cli` validates project names before generating projects.

**Valid examples:**

```text
myproject
my_project
project123
```

**Invalid examples:**

```text
my-project
my project
123project
```

Project names must contain only letters, numbers, and underscores, and must not start with a number.

## 👨‍💻 Author

**Mohamed Ali Ismail Jami**

Creator and maintainer of `projectstarter-cli`.

### Contact

- **GitHub:** https://github.com/hamada-cool
- **Repository:** https://github.com/hamada-cool/projectstarter
- **Issues and bug reports:** https://github.com/hamada-cool/projectstarter/issues
- **Email:** mohamedali32947@gmail.com
- **Phone / WhatsApp:** +918341391506 / +249919532947

For bug reports, feature requests, or suggestions, you can open an issue in the GitHub repository.

## 🤝 Contributing

Contributions, bug reports, suggestions, and improvements are welcome!

### Contribution Workflow

1. Fork the repository.
2. Create a branch for your changes.
3. Implement and test your changes.
4. Run the test suite.
5. Commit and push your changes.
6. Open a pull request.

Run the tests before submitting your changes:

```bash
python -m pytest
```

## 📄 License

`projectstarter-cli` is released under the MIT License.

See the [LICENSE](https://github.com/hamada-cool/projectstarter/blob/main/LICENSE) file for the full license text.

## 🎯 Project Status

Currently supported generators:

- Python
- Django
- Flask
- FastAPI

The project is under active development, and additional generators and features may be introduced in future releases.

**Latest release:** [v0.1.2](https://github.com/hamada-cool/projectstarter/releases/tag/v0.1.2)

## ⭐ Support the Project

If you find `projectstarter-cli` useful, you can help support its development by:

- ⭐ Starring the [GitHub repository](https://github.com/hamada-cool/projectstarter).
- 🐛 Reporting bugs.
- 💡 Suggesting new features.
- 🤝 Contributing code.
- 📢 Sharing the project with other developers.

---

**projectstarter-cli — Start your next Python project faster. 🚀**

Created by **Mohamed Ali Ismail Jami**.
