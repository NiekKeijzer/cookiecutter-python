"""
Defines the project's version and methods to get
 the version in a uniform manner.
"""
import toml

from .constants import PROJECT_DIRECTORY


def get_version() -> str:
    """
    Return the PyProject version for usage in Python.

    Using the pyproject.toml file for this ensure the version is defined
     in a single location which in turn prevents issues with mismatched
     versions.
    """
    pyproject_file = PROJECT_DIRECTORY / "pyproject.toml"
    pyproject = toml.load(pyproject_file.open())

    return str(pyproject['tool']['poetry']['version'])


__version__ = get_version()
