from pathlib import Path
from typing_extensions import Annotated

import json
import typer

app = typer.Typer()


@app.command(short_help="Remove a configuration from the database")
def remove(
    config_path: Annotated[
        Path,
        typer.Argument(
            help="The configuration's path",
            show_default=False,
        ),
    ],
):
    """
    Remove a configuration from the database.
    If CONFIG_PATH is relative,
    will query the path as '$PWD/CONFIG_PATH'
    """
    db_file_path = Path.home() / ".local/share/dotmgr/db.json"

    db: [str] = []

    if db_file_path.exists():
        with open(db_file_path) as db_file:
            db: list = json.load(db_file)

    filtered_db_path = [
        path for path in db if Path(path) != config_path.absolute()
    ]

    with open(db_file_path, "w") as db_file:
        json.dump(filtered_db_path, db_file)
