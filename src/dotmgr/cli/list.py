import typer

app = typer.Typer()


@app.command()
def list():
    print("Listing of all the configuration")
