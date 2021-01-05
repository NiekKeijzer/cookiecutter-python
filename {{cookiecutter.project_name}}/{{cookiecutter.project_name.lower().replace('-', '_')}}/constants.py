"""
Constants and paths that should be defined and _never_ changed during the
 runtime.
"""
import pathlib

PACKAGE_DIRECTORY = pathlib.Path(__file__).parent
PROJECT_DIRECTORY = PACKAGE_DIRECTORY / ".."
TEMP_DIRECTORY = PROJECT_DIRECTORY / "var"
