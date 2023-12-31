# Advent of Code Getter

A simple program to retrieve [Advent of Code](https://adventofcode.com) inputs   

## How to run

1. If you haven't already, install [git](https://git-scm.com/downloads) and [python](https://www.python.org/downloads/)
2. Run in a terminal `git clone https://github.com/gdar463/aoc-getter.git`
3. Run in a terminal `cd aoc-getter`
4. Run in a terminal `pip install -r requirements.txt`
5. If you're on Windows run `py main.py`
    5a. If you're on Mac or Linux run `python3 main.py`

## How to get your session token

1. Open in your browser [https://adventofcode.com](https://adventofcode.com)
2. Press `F12` on your keyboard
    2a. If a new part in your browser doesn't appear, try to press `Fn + F12`
3. On the new part go in the `Storage` or `Application` tab, depending on the browser
4. Find on the left list `Cookies`, open the dropdown menu and select the first item
5. Double-click on the value of `session` in the right list and copy all the text
6. When the program asks paste it in

***BE CAREFUL!***
Don't share your token with anyone. If you want to check how your token is used follow the usage of the `token` variable in [main.py](main.py) from line 23

## Parameters

| Name          | Description                                         | Required | Value                                                                                           |
|---------------|-----------------------------------------------------|----------|-------------------------------------------------------------------------------------------------|
| Year          | Year of the input(s) wanted                         | Yes      | Obtained at run-time                                                                            |
| Day(s)        | Day (or days) of the input(s) wanted                | Yes      | Obtained at run-time                                                                            |
| Session Token | Your session token for the website                  | Yes      | Obtained from the enviromental variable `AOC_TOKEN` or run-time if not set                      |
| Download Path | Where the inputs will be stored                     | Yes      | Obtained from the enviromental variable `AOC_DOWNLOAD_PATH` or run-time if not set              |
| Cache Path    | Where the cache will be stored                      | No       | By default `<this project root>/cache` or, if set, the enviromental variable `AOC_CACHE_PATH`   |
| API Website   | The website from where the inputs will ve requested | No       | By default `https://adventofcode.com` or, if set, the enviromental variable `AOC_API`           |

## Parameters' Rules

The inputs will be stored in `<Download Path>/<year>/<day>/input`    
The cache will be stored in `<Cache Path>/cache`   
The cached items will be stored in `<Cache Path>/<random sha1 hash>`   
The inputs will be requested in the format of `<API Website>/<year>/day/<day>/input` (if the website uses a different format than default, change line 14 in src/interface.py to reflect it)   
   
You can request a single day setting Day(s) to a number (es. `1`, `14`, `19`), or multiple days using the format `<first day>-<last day>`   
If you request multiple days it might take, a while before the inputs will be downloaded (between each request there's a sleep of 4 minutes). So be patient.
If you don't know how to obtain your Session Token check the How to get your session token in the README.md file or go to [How to get your session token](#How-to-get-your-session-token)   
If you have `AOC_API` set, you have to confirm that you want to use it as API Website, by typing Y when asked   
   
## Automation Rules

This script uses the following strategies to comply with the [Automation Guidelines](https://www.reddit.com/r/adventofcode/wiki/faqs/automation) found on the [r/adventofcode](https://www.reddit.com/r/adventofcode)'s wiki:
* When multiple days are retrieved, line 48 in [src/interface.py](src/interface.py) will wait 4 minutes between requests
* All of [src/cache.py](src/cache.py) file is dedicated for writing to and retrieve from the cache
* The `User-Agent` header is specified on line 9 in [src/interface.py](src/interface.py) and use on line 16
