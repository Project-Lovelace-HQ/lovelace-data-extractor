from invoke import task


@task
def run(c):
    c.run("python src/main.py")


@task
def lint(c):
    c.run("black .")


@task
def test(c):
    c.run("pytest")


@task
def coverage(c):
    c.run("pytest --cov=src --cov-report html")
