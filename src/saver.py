import os
from pathlib import Path


def save_file(year: str, day: str, download_path: Path, body: str):
    path = Path(os.path.expanduser(os.path.expandvars(str(download_path).replace("\"", ""))))
    if not os.path.isdir(path.joinpath(year, day)):
        os.makedirs(path.joinpath(year, day))
    with open(path.joinpath(year, day, "input"), "w") as f:
        f.write(body)


def save_files(year: str, days: list[str], download_path: Path, bodies: list[str]):
    for i, day in enumerate(days):
        save_file(year, day, download_path, bodies[i])
