from projectstarter.generator import create_python_project , create_flask_project, create_django_project, create_fastapi_project

def test_create_python_project(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    create_python_project("testproject")

    project = tmp_path /"testproject"

    assert project.exists()
    assert (project / "src").exists()
    assert (project / "tests").exists()

    assert (
        project / "src" / "testproject" / "__init__.py"
    ).exists()

    assert (
        project / "src" / "testproject" / "main.py"
    ).exists()

    assert (
        project / "tests" / "test_main.py"
    ).exists()

    assert (project / ".gitignore").exists()
    assert (project / "requirements.txt").exists()
    assert (project / "README.md").exists()

def test_create_flask_project(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    create_flask_project("flasktest")

    project = tmp_path / "flasktest"

    assert project.exists()
    assert(project / "app").exists()
    assert(project / "app" / "__init__.py").exists()
    assert(project / "app" / "templates").exists()
    assert(project / "app" / "static").exists()
    assert(project / "run.py").exists()
    assert (project / "requirements.txt").exists()
    assert (project / ".gitignore").exists()
    assert (project / "README.md").exists()

def test_create_django_project(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    create_django_project("djangotest")

    project = tmp_path / "djangotest"

    assert project.exists()
    assert (project / ".venv").exists()
    assert (project / "manage.py").exists()
    assert (project / "config").exists()
    assert (project / "config" / "settings.py").exists()
    assert (project / "config" / "urls.py").exists()
    assert (project / "config" / "asgi.py").exists()
    assert (project / "config" / "wsgi.py").exists()

    assert (project / "requirements.txt").exists()
    assert (project / ".gitignore").exists()
    assert (project / "README.md").exists()

def test_create_fastapi_project(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    create_fastapi_project("apitest")

    project = tmp_path / "apitest"

    assert project.exists()
    assert(project / ".venv").exists()
    assert(project / "app").exists()
    assert(project / "app" / "__init__.py").exists()
    assert(project / "app" / "main.py").exists()

    assert(project / "requirements.txt").exists()
    assert(project / ".gitignore").exists()
    assert(project / "README.md").exists()

    