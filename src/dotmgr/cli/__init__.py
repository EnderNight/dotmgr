import typer

from .add import app as add_app
from .snapshot import app as snapshot_app
from .list import app as list_app
from .remove import app as remove_app

app = typer.Typer(no_args_is_help=True, add_completion=False)


app.add_typer(add_app)
app.add_typer(remove_app)
app.add_typer(snapshot_app)
app.add_typer(list_app)
