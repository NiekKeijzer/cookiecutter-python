import toml

from .constants import PROJECT_DIRECTORY


def get_version():
    pyproject_file = PROJECT_DIRECTORY / "pyproject.toml"
    pyproject = toml.load(pyproject_file.open())

    return pyproject['tool']['poetry']['version']


__version__ = get_version()
