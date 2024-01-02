from hashlib import sha256

import requests
import time

import src.cache as cache
import src.env_var as env_var
import src.saver as saver
from src.exceptions import InputNotFoundException, InvalidSessionTokenException, ServerErrorException, custom_raise

userAgent = "github.com/gdar463/aoc-getter by gdar463@gmail.com"


def get_input_from_site(year: str, day: str, token: str, api_server: str) -> requests.Response:
    request = requests.request("GET",
                               api_server.replace("\"", "") + "/" + year + "/day/" + day + "/input",
                               headers = {
                                   "user-agent": userAgent
                               },
                               cookies = {
                                   "session": token
                               })
    if request.status_code == 200:
        return request
    elif request.status_code == 400:
        custom_raise(InvalidSessionTokenException)
    elif request.status_code == 404:
        custom_raise(InputNotFoundException, request.text)
    else:
        custom_raise(ServerErrorException, request.status_code, request.text)


def get_input(year: str, day: str, token: str, api_server: str):
    download_path = env_var.get_download_path()
    token_hash = sha256(token.encode()).hexdigest()
    cached = cache.check_cache(year, day, token_hash)
    if type(cached) is str:
        with open(cache.get_cache_path().joinpath(cached), "rt") as f:
            body = f.read()
        saver.save_file(year, days, download_path, body)
    else:
        day_input = get_input_from_site(year, day, token, api_server).text
        cache.write_cache(year, day, token_hash, day_input)
        saver.save_file(year, day, download_path, day_input)


def get_inputs(year: str, days: list[str], token: str, api_server: str):
    for i, day in enumerate(days):
        if i != 0:
            time.sleep(240)
        get_input(year, day, token, api_server)
