from pathlib import Path
from typing_extensions import Annotated

import json
import typer

app = typer.Typer()


@app.command()
def remove(config: Annotated[Path, typer.Argument()]):
    db_file_path = Path.home() / ".local/share/dotmgr/db.json"

    db: [str] = []

    if db_file_path.exists():
        with open(db_file_path) as db_file:
            db: list = json.load(db_file)

    filtered_db_path = [str(path) for path in db if Path(path) != config.absolute()]

    with open(db_file_path, "w") as db_file:
        json.dump(filtered_db_path, db_file)
