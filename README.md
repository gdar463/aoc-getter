# Advent of Code Getter

A simple program to retrieve [Advent of Code](https://adventofcode.com) inputs   

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
If you have `AOC_API` set, you have to confirm that you want to use it as API Website, by typing Y when asked   
   
## Automation Rules

This script uses the following strategies to comply with the [Automation Guidelines](https://www.reddit.com/r/adventofcode/wiki/faqs/automation) found on the [r/adventofcode](https://www.reddit.com/r/adventofcode)'s wiki:
* When multiple days are retrieved, line 48 in [src/interface.py](src/interface.py) will wait 4 minutes between requests
* All of [src/cache.py](src/cache.py) file is dedicated for writing to and retrieve from the cache
* The `User-Agent` header is specified on line 9 in [src/interface.py](src/interface.py) and use on line 16
