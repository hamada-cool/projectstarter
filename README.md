# projectstarter-cli 🚀

projectstarter-cli is a Python CLI tool created by **Mohamed Ali Ismail Jami** for quickly creating ready-to-use project structures.

It helps developers avoid manually creating folders, files, virtual environments, installing framework dependencies, and preparing basic project documentation.

## ✨ Features

- 🐍 Create basic Python projects
- 🌐 Create Django projects
- ⚡ Create Flask projects
- 🚀 Create FastAPI projects
- 📦 Automatically create `.venv` for Django, Flask, and FastAPI projects
- ⬆️ Automatically upgrade `pip`
- 🔧 Automatically install required framework packages
- 📄 Automatically generate `requirements.txt`
- 🚫 Automatically generate `.gitignore`
- 📝 Automatically generate a README for generated projects
- 📋 List supported project types
- ℹ️ Show information about each project type
- 🩺 Check the projectstarter-cli installation with `doctor`
- 🧪 Includes automated tests

---

## 📋 Supported Project Types

| Project Type | Virtual Environment | Automatic Dependency Installation | Run Command |
|---|---|---|---|
| Python | No | No | `python src/<project_name>/main.py` |
| Django | Yes | Yes | `python manage.py runserver` |
| Flask | Yes | Yes | `python run.py` |
| FastAPI | Yes | Yes | `uvicorn app.main:app --reload` |

> The basic Python generator creates the project structure directly. Django, Flask, and FastAPI projects receive their own `.venv` and framework dependencies automatically.

---

# 📦 Installation

Install projectstarter-cli from PyPI:

```bash
pip install projectstarter-cli
```

Check that it is installed:

```bash
projectstarter --version
```

Show the available commands:

```bash
projectstarter --help
```

---

# 🚀 Usage

## 1. Create a project interactively

Run:

```bash
projectstarter create
```

projectstarter-cli will show the available project types:

```text
Choose a project type:

1. python
2. django
3. flask
4. fastapi
```

Then enter the number of the project type and the project name.

Example:

```text
Enter your choice: 2
Enter project name: myproject
```

projectstarter-cli will create the project automatically.

---

## 2. Create a Python project

Run:

```bash
projectstarter create python myproject
```

The generated structure is:

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

### Run the Python project

Windows:

```powershell
python src/myproject/main.py
```

The generated application contains a simple `main()` function.

---

# 🌐 Django

Create a Django project:

```bash
projectstarter create django myproject
```

projectstarter-cli automatically:

1. Creates the project directory.
2. Creates `.venv`.
3. Upgrades `pip`.
4. Installs Django.
5. Creates the Django project using the `config` package.
6. Creates `requirements.txt`.
7. Creates `.gitignore`.
8. Creates a project README.

The main structure is:

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

### Activate the virtual environment

Windows:

```powershell
cd myproject
.venv\Scripts\activate
```

macOS/Linux:

```bash
cd myproject
source .venv/bin/activate
```

### Run Django

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

# ⚡ Flask

Create a Flask project:

```bash
projectstarter create flask myproject
```

projectstarter-cli automatically:

1. Creates the project directory.
2. Creates `.venv`.
3. Upgrades `pip`.
4. Installs Flask.
5. Creates the `app` package.
6. Creates `templates` and `static` directories.
7. Creates `run.py`.
8. Creates `requirements.txt`.
9. Creates `.gitignore`.
10. Creates a project README.

The generated structure is:

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

### Activate the virtual environment

Windows:

```powershell
cd myproject
.venv\Scripts\activate
```

macOS/Linux:

```bash
cd myproject
source .venv/bin/activate
```

### Run Flask

```bash
python run.py
```

Open:

```text
http://127.0.0.1:5000/
```

---

# 🚀 FastAPI

Create a FastAPI project:

```bash
projectstarter create fastapi myproject
```

projectstarter-cli automatically:

1. Creates the project directory.
2. Creates `.venv`.
3. Upgrades `pip`.
4. Installs FastAPI.
5. Installs Uvicorn.
6. Creates the `app` package.
7. Creates `app/main.py`.
8. Creates `requirements.txt`.
9. Creates `.gitignore`.
10. Creates a project README.

The generated structure is:

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

### Activate the virtual environment

Windows:

```powershell
cd myproject
.venv\Scripts\activate
```

macOS/Linux:

```bash
cd myproject
source .venv/bin/activate
```

### Run FastAPI

```bash
uvicorn app.main:app --reload
```

API:

```text
http://127.0.0.1:8000/
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 📋 List Project Types

To see all available generators:

```bash
projectstarter list
```

Example:

```text
Available project types:

  python
  django
  flask
  fastapi
```

---

# ℹ️ Project Information

Use the `info` command to see information about a generator.

Example:

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

You can also check other project types:

```bash
projectstarter info python
projectstarter info flask
projectstarter info fastapi
```

---

# 🩺 Doctor

projectstarter-cli includes a built-in diagnostic command:

```bash
projectstarter doctor
```

It checks:

- Python
- Project registry
- Available generators
- Project information

Example:

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

---

# 🧪 Testing projectstarter-cli

projectstarter-cli uses `pytest` for automated testing.

Install pytest for development:

```bash
python -m pip install pytest
```

Run all tests:

```bash
python -m pytest
```

The test suite covers:

- Project name validation
- Generator registry
- Project information
- Python project generation
- Django project generation
- Flask project generation
- FastAPI project generation
- CLI commands
- Interactive project creation
- Doctor command

---

# 🏗️ projectstarter-cli Development Structure

The projectstarter-cli source code is organized as follows:

```text
projectstarter/
├── projectstarter/
│   ├── __init__.py
│   ├── cli.py
│   ├── doctor.py
│   ├── generator.py
│   ├── registry.py
│   └── utils.py
│
├── templates/
│   └── python/
│       └── main.py
│
├── tests/
│   ├── test_cli.py
│   ├── test_generator.py
│   ├── test_registry.py
│   └── test_utils.py
│
├── README.md
├── LICENSE
└── pyproject.toml
```

## Main Components

### `cli.py`

Handles the command-line interface and commands such as:

```text
create
list
info
doctor
--version
```

### `generator.py`

Contains the project generation logic for:

- Python
- Django
- Flask
- FastAPI

It also handles virtual environment creation and dependency installation for supported frameworks.

### `registry.py`

Contains the registered project generators and project information.

### `utils.py`

Contains utility functions such as project-name validation.

### `doctor.py`

Provides the `projectstarter doctor` diagnostic command.

### `tests/`

Contains the automated test suite.

---

# ➕ Adding a New Generator

projectstarter-cli is designed so that new project types can be added to the generator system.

A new generator generally needs:

1. A generator function in `generator.py`.
2. Registration in `registry.py`.
3. Project information in `PROJECT_INFO`.
4. Tests in `tests/test_generator.py`.
5. CLI tests when necessary.
6. Documentation in this README.

This keeps the CLI organized and makes the tool easier to extend.

---

# 🔐 Project Name Rules

projectstarter-cli validates project names before creating projects.

Valid examples:

```text
myproject
my_project
project123
```

Invalid examples:

```text
my-project
my project
123project
```

Project names must use letters, numbers, and underscores and must not start with a number.

---

# 👨‍💻 Author

**Mohamed Ali Ismail Jami**

projectstarter-cli was created and is maintained by Mohamed Ali Ismail Jami.

## 📞 Contact

For questions, suggestions, bug reports, or contributions, contact the project maintainer through GitHub.

- GitHub: https://github.com/hamada-cool
- Project Repository: https://github.com/hamada-cool/projectstarter
- Bug Reports / Issues: https://github.com/hamada-cool/projectstarter/issues
- Email: `mohamedali32947@gmail.com`
- Phone / WhatsApp: `+918341391506` and `+249919532947`

You can also open a GitHub Issue if you find a bug or have an idea for improving projectstarter-cli.

---

# 🤝 Contributing

Contributions, bug reports, suggestions, and improvements are welcome.

Before submitting changes:

1. Create a branch for your change.
2. Make your changes.
3. Run the test suite.
4. Make sure all tests pass.
5. Open a pull request.

Run tests with:

```bash
python -m pytest
```

---

# 📄 License

projectstarter-cli is licensed under the **MIT License**.

See the `LICENSE` file for the complete license text.

---

# 🎯 Project Status

projectstarter-cli currently supports:

- Python
- Django
- Flask
- FastAPI

The project is under active development, and more generators and features may be added in future releases.

---

## ⭐ Support the Project

If you find projectstarter-cli useful, you can support the project by:

- ⭐ Starring the GitHub repository
- 🐛 Reporting bugs
- 💡 Suggesting features
- 🤝 Contributing code
- 📢 Sharing the project with other developers

---

**projectstarter-cli — Start your next Python project faster. 🚀**

Created by **Mohamed Ali Ismail Jami**.
