import os
import sys
from typing import Tuple

# setup function must run only if setup.py is running as a script
try:
    import setup
except SystemExit:
    print(f'You have to wrap setup(...) call with: if __name__ == "__main__"', file=sys.stderr)
    sys.exit(1)


def check_import_variables(required_vars: Tuple[str]):
    missing_vars = [varname for varname in required_vars if not hasattr(setup, varname)]
    if missing_vars:
        print(f"Variables not found in setup.py: {missing_vars}", file=sys.stderr)
        sys.exit(1)


required_vars = ("MODULE_NAME", "REQUIREMENTS_FILE", "SETUP_ARGS")


check_import_variables(required_vars)

from setup import MODULE_NAME, REQUIREMENTS_FILE, SETUP_ARGS

# MODULE_NAME must be the repository name
repo_name = "cfdibills"

assert repo_name == MODULE_NAME, f'REPO_NAME != "{repo_name}"'

# There must be a VERSION file in folder libname/VERSION
assert "VERSION" in os.listdir(f"{MODULE_NAME}/"), f'Cannot find file "{MODULE_NAME}/VERSION"'

# REQUIREMENTS_FILE must be 'requirements.in'
assert REQUIREMENTS_FILE == "requirements.in", f'REQUIREMENTS_FILE must be "requirements.in"'

# Check SETUP_ARGS keys
required = (
    "name",
    "url",
    "author",
    "packages",
    "keywords",
    "license",
    "version",
    "install_requires",
    "extras_require",
    "classifiers",
)

missing = sorted(list(set(required) - set(SETUP_ARGS.keys())))
assert not missing, f"Not all required keys were found in SETUP_ARGS: {missing}"


print("Everything ok with setup.py!")
