import shutil
from invoke import task


@task
def run(c):
    c.run("func start")


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
    shutil.rmtree("coverage", ignore_errors=True)
    c.run(
        "pytest --cov=src --cov-report=xml:coverage/coverage.xml --cov-report=html:coverage"
    )


@task
def requirements(c):
    c.run("pipenv requirements > requirements.txt")
