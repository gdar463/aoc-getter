import json
import os
import random
from pathlib import Path

import src.env_var as env_var


# cache file format:
# {
#     "<token-sha256>": {
#         "<year>": {
#             "<day>": "<random-sha1>"
#         }
#     }
# }


def get_cache_path() -> Path:
    path = env_var.get_cache_path()
    if not os.path.isdir(path):
        # noinspection PyBroadException
        try:
            os.makedirs(path)
        except Exception as e:
            # stupid error
            pass
    if not os.path.isfile(path.joinpath("cache")):
        open(path.joinpath("cache"), "x").close()
    return path


def check_cache(year: str, day: str, token_hash: str) -> str | None:
    path = get_cache_path().joinpath("cache")
    with open(path, "r+") as f:
        # noinspection PyBroadException
        try:
            cache: dict = json.load(f)
        except Exception as e:
            cache: dict = {}
    if token_hash in cache:
        if year in cache[token_hash]:
            if day in cache[token_hash][year]:
                return str(cache[token_hash][year][day])
            else:
                return None
        else:
            return None
    else:
        return None


def write_cache(year: str, day: str, token_hash: str, body: str):
    with open(get_cache_path().joinpath("cache"), "rt") as f:
        file = f.read()
        if len(file) != 0:
            cache: dict = json.loads(file)
        else:
            cache: dict = {}
    hashed = random.randbytes(32).hex()
    with open(get_cache_path().joinpath(hashed), "x") as h:
        h.write(body)
    if token_hash not in cache:
        cache[token_hash] = {}
    if year not in cache[token_hash]:
        cache[token_hash][year] = {}
    cache[token_hash][year][day] = hashed
    with open(get_cache_path().joinpath("cache"), "wt") as j:
        json.dump(cache, j)
