from pathlib import Path
from typing_extensions import Annotated

import json
import typer

app = typer.Typer()


@app.command(short_help="Add a new configuration in the database")
def add(
    config_path: Annotated[
        Path,
        typer.Argument(
            help="The configuration's path",
            show_default=False,
        ),
    ],
):
    """
    Add a new configuration in the database.
    If CONFIG_PATH is relative,
    will store the path as '$PWD/CONFIG_PATH'
    """

    app_dir = Path.home() / ".local/share/dotmgr"
    db_file_path = app_dir / "db.json"
    db: [str] = []

    app_dir.mkdir(parents=True, exist_ok=True)

    if db_file_path.exists():
        with open(db_file_path) as db_file:
            db: list = json.load(db_file)

    db.append(str(config_path.absolute()))

    with open(db_file_path, "w") as db_file:
        json.dump(db, db_file)
