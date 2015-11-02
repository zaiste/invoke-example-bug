from invoke import task

@task
def unit():
    print("Running unit tests!")

@task
def integration():
    print("Running integration tests!")