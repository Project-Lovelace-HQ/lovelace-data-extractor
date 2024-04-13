import shutil
from invoke import task


@task
def run(c):
    shutil.rmtree("output", ignore_errors=True)
    c.run("python src/main.py")


@task
def lint(c):
    c.run("black .")


@task
def bumpversion(c, part):
    """
    Bump the version number of the project.

    The `part` parameter should be either
    'major', 'minor' or 'patch'
    """
    c.run(f"bump2version {part}")


@task
def test(c):
    c.run("pytest")


@task
def coverage(c):
    shutil.rmtree("htmlcov", ignore_errors=True)
    c.run("pytest --cov=src --cov-report html")
