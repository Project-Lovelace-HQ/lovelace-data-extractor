from invoke import task


@task
def run(c):
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
    c.run("pytest --cov=src --cov-report html")
