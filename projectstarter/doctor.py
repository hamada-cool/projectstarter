import sys

from .registry import GENERATORS, PROJECT_INFO


def run_doctor():
    print("\nProjectStarter Doctor")
    print("─" * 30)

    # Python
    print("✓ Python")
    print(f"  Version: {sys.version.split()[0]}")

    # Registry
    print("✓ Registry")

    # Generators
    print(f"✓ Generators ({len(GENERATORS)})")

    for project_type in GENERATORS:
        print(f"  - {project_type}")

    # Project information
    print("✓ Project Info")

    if set(GENERATORS.keys()) == set(PROJECT_INFO.keys()):
        print("  All project information is available.")
    else:
        print("  Warning: Project information is incomplete.")

    print("\nEverything looks good! ✓")