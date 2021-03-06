"""Configuration of nox for testing & code validation."""

import nox
from nox.sessions import Session

PYTHON_VERSION = "3.8"


@nox.session(python=PYTHON_VERSION)
def lint(session: Session) -> None:
    """Runs linting checks."""
    session.install(
        "flake8",
        "flake8-docstrings",
        "flake8-import-order",
        "flake8-black",
        "darglint",
        "flake8-annotations",
        "flake8-quotes",
        "flake8-requirements",
        "pep8-naming",
    )
    session.run("flake8", "src/")
    session.run("flake8", "tests/")
    session.run("flake8", "generate_names.py")


@nox.session(python=PYTHON_VERSION)
def tests(session: Session) -> None:
    """Runs unit testing & generates coverage report."""
    session.install("pytest", "pytest-cov", "pytest-xdist")
    session.run("pip", "install", "-r", "requirements.txt")
    session.run("pytest", "--cov")


@nox.session(python=PYTHON_VERSION)
def coverage(session: Session) -> None:
    """Upload coverage data."""
    session.install("coverage", "codecov")
    session.run("coverage", "xml", "--fail-under=0")
    session.run("codecov")
