from pathlib import Path
from typing_extensions import Annotated

import json
import typer

app = typer.Typer()


@app.command()
def add(config: Annotated[Path, typer.Argument()]):
    app_dir = Path.home() / ".local/share/dotmgr"
    db_file_path = app_dir / "db.json"
    db: [str] = []

    app_dir.mkdir(parents=True, exist_ok=True)

    if db_file_path.exists():
        with open(db_file_path) as db_file:
            db: list = json.load(db_file)

    db.append(str(config.absolute()))

    with open(db_file_path, "w") as db_file:
        json.dump(db, db_file)
