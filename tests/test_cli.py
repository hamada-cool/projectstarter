from projectstarter.cli import main
from unittest.mock import MagicMock, patch

def test_list_command(capsys, monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        ["projectstarter","list"]
    )

    main()

    output = capsys.readouterr().out

    assert "python" in output
    assert "django" in output
    assert "flask" in output
    assert "fastapi" in output

def test_info_command(capsys, monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        ["projectstarter","info", "django"]
    )

    main()

    output = capsys.readouterr().out

    assert "Django" in output
    assert "Python web framework" in output
    assert "Virtual environment: Yes" in output
    assert "python manage.py runserver" in output
    assert "Automatic installation: Yes" in output

def test_doctor_command(capsys, monkeypatch):

    monkeypatch.setattr(
        "sys.argv",
        ["projectstarter", "doctor"]
    )

    main()

    output = capsys.readouterr().out

    assert "ProjectStarter Doctor" in output
    assert "Python" in output
    assert "Registry" in output
    assert "Generators (4)" in output
    assert "Project Info" in output
    assert "Everything looks good!" in output

def test_create_command(monkeypatch):

    monkeypatch.setattr(
        "sys.argv",
        ["projectstarter", "create", "python", "myproject"]
    )

    mock_generator = MagicMock()

    with patch.dict(
        "projectstarter.cli.GENERATORS",
        {"python":mock_generator},
        clear=False
    ):

        main()

        mock_generator.assert_called_once_with(
            "myproject"
        )

def test_interactive_create(monkeypatch):

    monkeypatch.setattr(
        "sys.argv",
        ["projectstarter", "create"]
    )

    inputs = iter([
        "1",
        "myproject",
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs)
    )

    mock_generator = MagicMock()

    with patch.dict(
        "projectstarter.cli.GENERATORS",
        {"python": mock_generator},
        clear=False
    ):
        main()

    mock_generator.assert_called_once_with(
        "myproject"
    )