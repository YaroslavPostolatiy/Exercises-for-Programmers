from invoke import task


@task
def validate_code(c):
    c.run("pre-commit install")
    c.run("pre-commit run --all-files")


@task
def task(c, number):
    c.run(f"python {number}.py")
