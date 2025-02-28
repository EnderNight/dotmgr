
import typer

app = typer.Typer()


@app.command()
def snapshot():
    print("Generating a snapshot of the current configurations")
