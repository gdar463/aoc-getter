import os
from getpass import getpass
from pathlib import Path


def get_token() -> str:
    if "AOC_TOKEN" not in os.environ:
        print("You don't seem to have your aoc session token as \"AOC_TOKEN\" enviromental variable. "
              "If you want you can input it here to be added in the variable.")
        token = getpass("Token (from the website): ")
        os.environ["AOC_TOKEN"] = token
        return token
    else:
        return os.environ["AOC_TOKEN"]


def get_download_path() -> Path:
    if "AOC_DOWNLOAD_PATH" not in os.environ:
        print("You don't seem to have your download path as \"AOC_DOWNLOAD_PATH\" enviromental variable. "
              "If you want you can input it here to be added in the variable. "
              "(If you want you can use ~ as your user folder or vars (such as \"%AppData\" on Windows))")
        folder = Path(os.path.expandvars(os.path.expanduser(input("Download Path: "))))
        os.environ["AOC_DOWNLOAD_PATH"] = str(folder)
        return folder
    else:
        return Path(os.path.expandvars(os.path.expanduser(os.environ["AOC_DOWNLOAD_PATH"])))


def get_api_server() -> str:
    if "AOC_API" not in os.environ:
        return "https://adventofcode.com/"
    else:
        print("You seem to have the \"AOC_API\" enviromental variable")
        selected = input("Do you want to use it as the API Website? (Y or N) ")
        return os.environ["AOC_API"] if selected == "Y" else "https://adventofcode.com/"


def get_cache_path() -> Path:
    if "AOC_CACHE_PATH" not in os.environ:
        return Path(os.getcwd()).joinpath("cache")
    else:
        return Path(os.path.expandvars(os.path.expanduser(os.environ["AOC_CACHE_PATH"])))
