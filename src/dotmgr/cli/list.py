from pathlib import Path
from rich import print

import json
import typer

app = typer.Typer()


@app.command(name="list")
def list_config():
    db_file_path = Path.home() / ".local/share/dotmgr/db.json"

    db: [str] = []

    if db_file_path.exists():
        with open(db_file_path) as db_file:
            db: list = json.load(db_file)

    print(db)
