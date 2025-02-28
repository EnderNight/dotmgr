import typer

from .add import app as add_app
from .snapshot import app as snapshot_app
from .list import app as list_app

app = typer.Typer()


app.add_typer(add_app)
app.add_typer(snapshot_app)
app.add_typer(list_app)
