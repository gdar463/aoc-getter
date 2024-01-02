import os
from pwinput import pwinput
from pathlib import Path
from colorama import Fore
from dotenv import load_dotenv, set_key, find_dotenv

load_dotenv()


def get_token() -> str:
    if "AOC_TOKEN" not in os.environ:
        print("\nYou don't seem to have your aoc session token as " + Fore.LIGHTBLUE_EX + "\"AOC_TOKEN\"" + Fore.RESET + " enviromental variable. \nIf you want you can input it here to be added in the variable.")
        token = pwinput("Token (from the website): ")
        set_key(get_env_file(), "AOC_TOKEN", token)
        return token
    else:
        return os.environ["AOC_TOKEN"]


def get_download_path() -> Path:
    if "AOC_DOWNLOAD_PATH" not in os.environ:
        print("\nYou don't seem to have your download path as " + Fore.LIGHTBLUE_EX + "\"AOC_DOWNLOAD_PATH\"" + Fore.RESET + " enviromental variable. \nIf you want you can input it here to be added in the variable. (If you want you can use " + Fore.LIGHTBLUE_EX + "\"~\"" + Fore.RESET + " as your user folder or vars (such as " + Fore.LIGHTBLUE_EX + "\"%AppData%\"" + Fore.RESET + " on Windows))")
        folder = Path(os.path.expandvars(os.path.expanduser(input("Download Path: "))))
        set_key(get_env_file(), "AOC_DOWNLOAD_PATH", str(folder))
        return folder
    else:
        return Path(os.path.expandvars(os.path.expanduser(os.environ["AOC_DOWNLOAD_PATH"])))


def get_api_server() -> str:
    if "AOC_API" not in os.environ:
        return "https://adventofcode.com"
    else:
        print("\nYou seem to have the " + Fore.LIGHTBLUE_EX + "\"AOC_API\"" + Fore.RESET + " enviromental variable.")
        selected = input("Do you want to use it as the API Website? (Y or N) ")
        return os.environ["AOC_API"] if selected == "Y" else "https://adventofcode.com"


def get_cache_path() -> Path:
    if "AOC_CACHE_PATH" not in os.environ:
        return Path(os.getcwd()).joinpath("cache")
    else:
        return Path(os.path.expandvars(os.path.expanduser(os.environ["AOC_CACHE_PATH"])))


def get_env_file() -> Path:
    env_path = find_dotenv()
    if env_path == "":
        return Path(os.getcwd()).joinpath(".env")
    else:
        return Path(env_path)
