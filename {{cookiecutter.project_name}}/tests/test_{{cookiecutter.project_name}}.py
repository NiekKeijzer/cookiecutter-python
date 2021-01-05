"""
Test basic {{ cookiecutter.project_name }} logic.
 Eg: does the version match the expected version?
"""
from {{cookiecutter.project_name.lower().replace('-', '_')}} import __version__


def test_version():
    """ Check if the defined version matches the expected version """
    assert __version__ == "0.1.0"
