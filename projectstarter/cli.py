import argparse

from .registry import GENERATORS, PROJECT_INFO
from .utils import validate_project_name
from .doctor import run_doctor

def main():
    parser = argparse.ArgumentParser(
        description="ProjectStarter - Create projects quickly"
    )

    parser.add_argument(
        "--version",
        action="version",
        version="ProjectStarter 0.1.0"
    )

    subparsers = parser.add_subparsers(
        dest="command"
    )

    # create command
    create_parser = subparsers.add_parser(
        "create",
        help="Create a new project"
    )

    create_parser.add_argument(
        "project_type",
        nargs="?",
        choices=GENERATORS.keys(),
        help="Type of project to create"
    )

    create_parser.add_argument(
        "project_name",
        nargs="?",
        help="Name of the project"
    )

    # list command
    subparsers.add_parser(
        "list",
        help="List available project types"
    )

    # info command
    info_parser = subparsers.add_parser(
        "info",
        help="Show information about a project type"
    )

    # doctor command
    subparsers.add_parser(
        "doctor",
        help="Check ProjectStarter installation"
    )

    info_parser.add_argument(
        "project_type",
        choices=PROJECT_INFO.keys(),
        help="Project type to show information about"
    )

    args = parser.parse_args()

    # create project
    if args.command == "create":

        try:

            if args.project_type is None:

                print("\nChoose a project type:\n")

                project_types = list(GENERATORS.keys())

                for index, project_type in enumerate(
                    project_types,
                    start=1
                ):
                    print(f"{index}. {project_type}")

                print()

                choice = input("Enter your choice: ")

                try:
                    choice = int(choice)
                    project_type = project_types[choice - 1]

                except (ValueError, IndexError):
                    print("Invalid choice.")
                    return

                project_name = input(
                    "Enter project name: "
                )

                if not validate_project_name(project_name):
                    print(
                        "Invalid project name."
                        "\nUse only letters, numbers, and underscores."
                        "\nProject name must not start with a number."
                    )
                    return

                generator = GENERATORS[project_type]

                generator(project_name)

            else:

                generator = GENERATORS[args.project_type]

                if args.project_name is None:
                    args.project_name = input(
                        "Enter project name: "
                    )

                if not validate_project_name(args.project_name):
                    print(
                        "Invalid project name."
                        "\nUse only letters, numbers, and underscores."
                        "\nProject name must not start with a number."
                    )
                    return

                generator(args.project_name)

        except FileExistsError as error:

            print(f"\nError: {error}")

    # list projects
    elif args.command == "list":

        print("\nAvailable project types:\n")

        for project_type in GENERATORS:
            print(f"  {project_type}")

        print()

    # info project
    elif args.command == "info":

        info = PROJECT_INFO[args.project_type]

        print(f"\n{args.project_type.capitalize()}")
        print("─" * 30)

        print(f"Description: {info['description']}")
        print(
            f"Virtual environment: "
            f"{info['virtual_environment']}"
        )
        print(
            f"Automatic installation: "
            f"{info['automatic_installation']}"
        )

        print("\nRun:")
        print(f"    {info['run']}")

        print()

    elif args.command == "doctor":
        run_doctor()


if __name__ == "__main__":
    main()