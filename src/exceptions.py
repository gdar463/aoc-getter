import enum
import os

import sys
from colorama import Fore


class Inputs(enum.StrEnum):
    YEAR = "Year"
    DAYS = "Days"


class InvalidInputException:
    def __init__(self, item: Inputs, error: str):
        message = Fore.LIGHTRED_EX + "The input " + Fore.LIGHTBLUE_EX + "\"" + error + "\"" + Fore.LIGHTRED_EX + " is invalid for " + Fore.LIGHTYELLOW_EX + str(item.value) + Fore.RESET
        sys.stderr.write(message)


class InputNotFormattedCorrectlyException:
    def __init__(self, item: Inputs, error: str):
        message = Fore.LIGHTRED_EX + "The input " + Fore.LIGHTBLUE_EX + "\"" + error + "\"" + Fore.LIGHTRED_EX + " isn't formatted correctly for " + Fore.LIGHTYELLOW_EX + str(item.value) + Fore.RESET
        sys.stderr.write(message)


class InvalidSessionTokenException:
    def __init__(self):
        message = Fore.LIGHTRED_EX + "The session token in the enviromental variable (or that you inputed) is invalid. " + Fore.LIGHTBLUE_EX + "\"AOC_API\"" + Fore.LIGHTRED_EX + " enviromental variable'll be reset" + Fore.RESET
        os.environ["AOC_TOKEN"] = ""
        sys.stderr.write(message)


class ServerErrorException:
    def __init__(self, status_code: int, body: str):
        message = Fore.LIGHTRED_EX + "The server responded with code " + Fore.LIGHTBLUE_EX + str(status_code) + Fore.LIGHTRED_EX + " and body of: \n" + Fore.LIGHTWHITE_EX + body + Fore.LIGHTRED_EX + "\nTry again in " + Fore.LIGHTCYAN_EX + "5-10" + Fore.LIGHTRED_EX + " minutes or check if the website is down" + Fore.RESET
        sys.stderr.write(message)


class InputNotFoundException:
    def __init__(self, body: str):
        message = Fore.LIGHTRED_EX + "The server responded with code " + Fore.LIGHTBLUE_EX + "404" + Fore.LIGHTRED_EX + ". Probably you're using a custom API website, if so be sure to include " + Fore.LIGHTCYAN_EX + "https://" + Fore.LIGHTRED_EX + " or " + Fore.LIGHTCYAN_EX + "http://" + Fore.LIGHTRED_EX + " and to not put the trailing slash. \nAlso be sure that the website uses the format " + Fore.LIGHTCYAN_EX + "\"" + Fore.LIGHTYELLOW_EX + "<API Website>" + Fore.LIGHTCYAN_EX + "/" + Fore.LIGHTYELLOW_EX + "<year>" + Fore.LIGHTCYAN_EX + "/day/" + Fore.LIGHTYELLOW_EX + "<day>" + Fore.LIGHTCYAN_EX + "/input\"" + Fore.LIGHTRED_EX + ". The response body is: \n" + Fore.LIGHTWHITE_EX + body + Fore.RESET
        sys.stderr.write(message)


def custom_raise(exception, *args):
    exception(*args)
    sys.exit()
