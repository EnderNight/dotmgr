import typer

app = typer.Typer()


@app.command()
def add():
    print("Adding a new configuration")
