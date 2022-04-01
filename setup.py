from setuptools import setup, find_packages
from pathlib import Path

# The directory containing this file
HERE = Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# How to manage version bumping: https://realpython.com/pypi-publish-python-package/#versioning-your-package
setup(
    name='cfdibilly',
    version='0.1.0.a1',
    description="Read and verify CFDI invoices via SAT's web service",
    long_description=README,
    long_description_content_type="text/markdown",
    license='LGPGLv3',
    license_file="LICENSE",
    author="Carlos Pegueros",
    author_email='peguerosdc@gmail.com',
    packages=find_packages('cfdibilly'),
    package_dir={'': 'cfdibilly'},
    package_data={
        'api': ['cache/*'],
        'cfdis.cfdi33': ['schema/*'],
        'cfdis.cfdi40': ['schema/*'],
    },
    url='https://github.com/peguerosdc/cfdibilly',
    keywords=["cfdi", "sat", "client", "mexico"],
    install_requires=[
        "suds==1.0.0",
        "xmlschema==1.10.0",
    ],
)