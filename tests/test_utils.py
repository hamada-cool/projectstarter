from projectstarter.utils import validate_project_name

def test_valid_project_name():
    assert validate_project_name("myproject")

def test_valid_project_name_with_underscores():
    assert validate_project_name("my_project")

def test_valid_project_name_with_numbers():
    assert validate_project_name("project123")

def test_valid_project_name_with_hyphen():
    assert not validate_project_name("my-project")

def test_valid_project_name_with_space():
    assert not validate_project_name("my project")

def test_valid_project_name_starting_with_number():
    assert not validate_project_name("123project")