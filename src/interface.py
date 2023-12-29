import time

import requests
import cache
from hashlib import sha256

userAgent = "github.com/gdar463/aoc-getter by gdar463@gmail.com"


def get_input_from_site(year: str, day: str, token: str) -> requests.Response:
    request = requests.request("GET",
                               "https://adventofcode.com/" + year + "/day/" + day + "/input",
                               headers = {
                                   "user-agent": userAgent
                               },
                               cookies = {
                                   "session": token
                               })
    if request.status_code == 200:
        return request


def get_input(year: str, day: str, token: str) -> str:
    token_hash = sha256(token.encode()).hexdigest()
    cached = cache.check_cache(year, day, token_hash)
    if cached is str:
        return cached
    else:
        day_input = get_input_from_site(year, day, token).text
        cache.write_cache(year, day, token_hash, day_input)
        return day_input


def get_inputs(year: str, days: list[str], token: str) -> list[str]:
    output: list[str] = []
    for day in days:
        output.append(get_input(year, day, token))
        time.sleep(240)
    return output
