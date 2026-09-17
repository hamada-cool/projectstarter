import re


def validate_project_name(project_name):
    """Validate a project name."""

    if not project_name:
        return False

    pattern = r"^[A-Za-z_][A-Za-z0-9_]*$"

    return bool(re.match(pattern, project_name))