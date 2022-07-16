from pathlib import Path
from typing import List

from setuptools import find_packages, setup

# Package name used to install via pip (shown in `pip freeze` or `conda list`)
MODULE_NAME = "cfdibills"

# The directory containing this file
HERE = Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# File to get direct dependencies from (used by pip)
REQUIREMENTS_FILE = "requirements.in"


def get_version() -> str:
    return (HERE / MODULE_NAME / "VERSION").read_text().strip()


def requirements_from_pip(filename: str) -> List[str]:
    with open(filename, "r") as pip:
        return [l.strip() for l in pip if not l.startswith("#") and l.strip()]


SETUP_ARGS = {
    "name": MODULE_NAME,
    "version": get_version(),
    "description": "Read and verify CFDI bills via SAT's web service",
    "long_description": README,
    "long_description_content_type": "text/markdown",
    "license": "LGPGLv3",
    "license_file": "LICENSE",
    "author": "Carlos Pegueros",
    "author_email": "peguerosdc@gmail.com",
    "packages": find_packages(exclude=["tests"]),
    "package_data": {
        "cfdibills": ["VERSION"],
    },
    "url": f"https://github.com/peguerosdc/{MODULE_NAME}",
    "keywords": ["cfdi", "facturacion", "sat", "mexico"],
    "install_requires": requirements_from_pip(REQUIREMENTS_FILE),
    "extras_require": {
        "dev": requirements_from_pip("requirements_dev.txt"),
        "test": requirements_from_pip("requirements_test.txt"),
    },
    "classifiers": [
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
}

if __name__ == "__main__":
    setup(**SETUP_ARGS)
