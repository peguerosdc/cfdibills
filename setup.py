from typing import List

from setuptools import setup, find_packages
from pathlib import Path

# The directory containing this file
HERE = Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# File to get direct dependencies from (used by pip)
REQUIREMENTS_FILE = "requirements.in"


def requirements_from_pip(filename: str) -> List[str]:
    with open(filename, "r") as pip:
        return [l.strip() for l in pip if not l.startswith("#") and l.strip()]


# How to manage version bumping: https://realpython.com/pypi-publish-python-package/#versioning-your-package
setup(
    name="cfdibills",
    version="0.1.0.a10",
    description="Read and verify CFDI invoices via SAT's web service",
    long_description=README,
    long_description_content_type="text/markdown",
    license="LGPGLv3",
    license_file="LICENSE",
    author="Carlos Pegueros",
    author_email="peguerosdc@gmail.com",
    packages=find_packages(),
    package_data={
        "cfdibills": ["api/cache/*", "cfdis/*/schema/*"],
    },
    url="https://github.com/peguerosdc/cfdibills",
    keywords=["cfdi", "sat", "client", "mexico"],
    install_requires=requirements_from_pip(REQUIREMENTS_FILE),
    extras_require={
        "dev": requirements_from_pip("requirements_dev.txt"),
    },
)
