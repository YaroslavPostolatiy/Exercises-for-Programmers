from invoke import task


@task
def test(c):
    print("pryvit")


@task
def validate_code(c):
    c.run("pre-commit install")
    c.run("pre-commit run --all-files")
