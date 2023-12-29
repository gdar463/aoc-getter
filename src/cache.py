from pathlib import Path
import json
import os
import platform
import random

# cache file format:
# {
#     "<token-sha256>": {
#         "<year>": {
#             "<day>": "<random-sha1>"
#         }
#     }
# }


def get_cache_path() -> Path:
    if platform.system() == "Windows":
        path = Path("%AppData%/gdar463/aoc-getter/")
    else:
        path = Path("~/.gdar463/aoc-getter/")
    if not os.path.isdir(path):
        os.mkdir(path)
    if not os.path.isfile(path.joinpath("cache")):
        open(path.joinpath("cache"), "x").close()
    return path


def check_cache(year: str, day: str, token_hash: str) -> str | None:
    with open(get_cache_path(), "r+") as f:
        cache: dict = json.load(f)
    if list(cache[token_hash][year].keys()).count(day) != 0:
        return str(cache[token_hash][year][day])
    else:
        return None


def write_cache(year: str, day: str, token_hash: str, body: str):
    with open(get_cache_path(), "r+t") as f:
        cache: dict = json.load(f)
        hashed = random.randbytes(32).hex()
        with open(get_cache_path().parent.joinpath(hashed), "x") as h:
            h.write(body)
        cache[token_hash][year][day] = hashed
        json.dump(cache, f)
