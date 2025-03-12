from pathlib import Path

import json
import tarfile
import typer

app = typer.Typer()


@app.command(short_help="Create a snapshot archive of saved configurations")
def snapshot():
    """
    Create a snapshot archive of saved configurations.
    """
    db_file_path = Path.home() / ".local/share/dotmgr/db.json"

    db: [str] = []

    if db_file_path.exists():
        with open(db_file_path) as db_file:
            db: list = json.load(db_file)

    with tarfile.open("dotfiles.tar.gz", "w:gz") as tar:
        for path in db:
            tar.add(path, arcname=Path(path).name)
