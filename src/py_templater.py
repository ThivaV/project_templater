"""This script creates a project structure based on user input."""

import os
from pathlib import Path  # pylint: disable=unused-import
import logging
import shutil

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")


def get_project_structure(project_name):
    """
    Returns the project structure based on the selected option.
    Define all project structures
    """
    structures = {
        "1": [
            ".github/workflows/.gitkeep",
            f"src/{project_name}/__init__.py",
            f"src/{project_name}/utils/__init__.py",
            f"src/{project_name}/config/__init__.py",
            f"src/{project_name}/components/__init__.py",
            f"src/{project_name}/config/configuration.py",
            f"src/{project_name}/pipeline/__init__.py",
            f"src/{project_name}/entity/__init__.py",
            f"src/{project_name}/constants/__init__.py",
            ".env",
            "config/config.yaml",
            "params.yaml",
            "dvc.yaml",
            "requirements.txt",
            "requirements-dev.txt",
            "setup.py",
            "app.py",
            "main.py",
            f"notebooks/{project_name}.ipynb",
            "data/master_data/.gitkeep",
            "data/processed_data/.gitkeep",
            "docs/img/.gitkeep",
            "docs/doc/.gitkeep",
            "models/.gitkeep",
            "scripts/.gitkeep",
            "templates/index.html",
        ],
        "2": [
            ".github/workflows/.gitkeep",
            ".env",
            "requirements.txt",
            "requirements-dev.txt",
            "setup.py",
            "app.py",
            "main.py",
            f"notebooks/{project_name}.ipynb",
            "data/master_data/.gitkeep",
            "data/processed_data/.gitkeep",
            "docs/img/.gitkeep",
            "docs/doc/.gitkeep",
            "models/.gitkeep",
            "scripts/.gitkeep",
            f"src/{project_name}/__init__.py",
        ],
        "3": [
            ".github/workflows/.gitkeep",
            "data/master_data/.gitkeep",
            "data/processed_data/.gitkeep",
            "models/.gitkeep",
            f"notebooks/{project_name}.ipynb",
            "requirements-dev.txt",
            "scripts/.gitkeep",
            ".env",
            "docs/img/.gitkeep",
            "docs/doc/.gitkeep",
        ],
        "4": [
            ".github/workflows/.gitkeep",
            ".env",
            "requirements.txt",
            "requirements-dev.txt",
            "app.py",
            "notebooks/.gitkeep",
            "data/master_data/.gitkeep",
            "data/processed_data/.gitkeep",
            "docs/img/.gitkeep",
            "docs/doc/.gitkeep",
            "models/.gitkeep",
            "scripts/.gitkeep",
            "src/__init__.py",
        ],
        "5": [
            ".github/workflows/.gitkeep",
            ".env",
            "requirements.txt",
            "requirements-dev.txt",
            "app.py",
            "notebooks/.gitkeep",
            "data/master_data/.gitkeep",
            "data/processed_data/.gitkeep",
            "docs/img/.gitkeep",
            "docs/doc/.gitkeep",
            "models/.gitkeep",
            "scripts/.gitkeep",
            "src/__init__.py",
        ],
        "6": [
            ".github/workflows/.gitkeep",
            ".env",
            "pyproject.toml",
            "app.py",
            "notebooks/.gitkeep",
            "data/.gitkeep",
            "docs/.gitkeep",
            "models/.gitkeep",
            "src/__init__.py",
            "tests/.gitkeep"
        ],
    }
    return structures


def create_files(project_path, files, project_opt):
    """
    Create the necessary files and directories for the project.
    """
    local_requirements_packages = [
        "ipython",
        "ipykernel",
        "ipywidgets",
        "tqdm",
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
        "python-dotenv",
        "python-box",
    ]
    if project_opt == "5":
        local_requirements_packages.append("kagglehub")

    template_pyproject = os.path.join(os.path.dirname(__file__), "pyproject.toml")

    for file in files:
        file_path = os.path.join(project_path, file)
        file_dir, file_name = os.path.split(file_path)

        if file_dir:
            os.makedirs(file_dir, exist_ok=True)
            logging.info("Creating directory: %s for the file: %s", file_dir, file_name)

        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            with open(file_path, "w", encoding="utf-8") as f:
                if file_name == "requirements-dev.txt":
                    f.write("\n".join(local_requirements_packages) + "\n")
                    logging.info("Creating file with items: %s", file_path)
                elif file_name == "pyproject.toml":
                    if os.path.exists(template_pyproject):
                        shutil.copy(template_pyproject, file_path)
                        logging.info("Copied pyproject.toml template to: %s", file_path)
                    else:
                        logging.warning(
                            "Template pyproject.toml not found at: %s",
                            template_pyproject,
                        )
                else:
                    logging.info("Creating empty file: %s", file_path)
        else:
            logging.info("%s already exists", file_name)


def main():
    """Main function to execute the script."""
    project_name = input("Enter the project name: ")
    project_path = input("Enter the project path: ")

    prompt = (
        "\nSelect the project structure:\n"
        "\t1 = Master project structure\n"
        "\t2 = Minimal project structure\n"
        "\t3 = Cookbooks\n"
        "\t4 = General\n"
        "\t5 = Kaggle competition\n"
        "\t6 = Poetry: Use pyproject.toml (no requirements.txt/setup.py)\n"
        "Enter the number: "
    )
    project_opt = input(prompt).strip()
    structures = get_project_structure(project_name)
    files = structures.get(project_opt, structures["2"])  # Default to minimal

    create_files(project_path, files, project_opt)


if __name__ == "__main__":
    main()
