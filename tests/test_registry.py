from projectstarter.registry import GENERATORS, PROJECT_INFO

def test_all_generators_exist():
    excepted = {
        "python",
        "django",
        "flask",
        "fastapi",
    }

    assert set(GENERATORS.keys()) == excepted

def test_all_project_info_exist():
    excepted = {
        "python",
        "django",
        "flask",
        "fastapi",
    }

    assert set(PROJECT_INFO.keys()) == excepted

def test_generators_and_project_info_match():
    assert set(GENERATORS.keys()) == set(PROJECT_INFO.keys())