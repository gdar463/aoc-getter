from colorama import Fore


def init_message():
    print()
    print("       " + Fore.LIGHTGREEN_EX + "Advent of Code Getter" + Fore.RESET + " | " + Fore.LIGHTRED_EX + "by gdar463" + Fore.RESET + "        ")
    print("          " + Fore.LIGHTCYAN_EX + "github.com/gdar463/aoc-getter" + Fore.RESET + "          ")
    print("A simple program to retrieve Advent of Code inputs")
    print()
    print(Fore.LIGHTMAGENTA_EX + "Parameters needed" + Fore.RESET)
    print(Fore.LIGHTCYAN_EX + "Name             Description                                            Required     Value" + Fore.RESET)
    print(Fore.LIGHTWHITE_EX + "Year             " + Fore.RESET + "Year of the input(s) wanted                            " + Fore.LIGHTGREEN_EX + "Yes          " + Fore.RESET + "Obtained at run-time")
    print(Fore.LIGHTWHITE_EX + "Day(s)           " + Fore.RESET + "Day (or days) of the input(s) wanted                   " + Fore.LIGHTGREEN_EX + "Yes          " + Fore.RESET + "Obtained at run-time")
    print(Fore.LIGHTWHITE_EX + "Session Token    " + Fore.RESET + "Your session token for the website                     " + Fore.LIGHTGREEN_EX + "Yes          " + Fore.RESET + "Obtained from the enviromental variable " + Fore.LIGHTBLUE_EX + "\"AOC_TOKEN\"" + Fore.RESET + " or run-time if not set")
    print(Fore.LIGHTWHITE_EX + "Download Path    " + Fore.RESET + "Where the inputs will be stored                        " + Fore.LIGHTGREEN_EX + "Yes          " + Fore.RESET + "Obtained from the enviromental variable " + Fore.LIGHTBLUE_EX + "\"AOC_DOWNLOAD_PATH\"" + Fore.RESET + " or run-time if not set")
    print(Fore.LIGHTWHITE_EX + "Cache Path       " + Fore.RESET + "Where the cache will be stored                         " + Fore.LIGHTRED_EX + "No           " + Fore.RESET + "By default " + Fore.LIGHTYELLOW_EX + "\"<this project root>/cache\"" + Fore.RESET + " or, if set, the enviromental variable " + Fore.LIGHTBLUE_EX + "\"AOC_CACHE_PATH\"" + Fore.RESET)
    print(Fore.LIGHTWHITE_EX + "API Website      " + Fore.RESET + "The website from where the inputs will ve requested    " + Fore.LIGHTRED_EX + "No           " + Fore.RESET + "By default " + Fore.LIGHTYELLOW_EX + "\"https://adventofcode.com\"" + Fore.RESET + " or, if set, the enviromental variable " + Fore.LIGHTBLUE_EX + "\"AOC_API\"" + Fore.RESET)
    print()
    print("The inputs will be stored in " + Fore.LIGHTCYAN_EX + "\"" + Fore.LIGHTYELLOW_EX + "<Download Path>" + Fore.LIGHTCYAN_EX + "/" + Fore.LIGHTYELLOW_EX + "<year>" + Fore.LIGHTCYAN_EX + "/" + Fore.LIGHTYELLOW_EX + "<day>" + Fore.LIGHTCYAN_EX + "/input\"" + Fore.RESET)
    print("The cache will be stored in " + Fore.LIGHTCYAN_EX + "\"" + Fore.LIGHTYELLOW_EX + "<Cache Path>" + Fore.LIGHTCYAN_EX + "/cache\"" + Fore.RESET)
    print("The cached items will be stored in " + Fore.LIGHTCYAN_EX + "\"" + Fore.LIGHTYELLOW_EX + "<Cache Path>" + Fore.LIGHTCYAN_EX + "/" + Fore.LIGHTYELLOW_EX + "<random sha1 hash>" + Fore.LIGHTCYAN_EX + "\"" + Fore.RESET)
    print("The inputs will be requested in the format of " + Fore.LIGHTCYAN_EX + "\"" + Fore.LIGHTYELLOW_EX + "<API Website>" + Fore.LIGHTCYAN_EX + "/" + Fore.LIGHTYELLOW_EX + "<year>" + Fore.LIGHTCYAN_EX + "/day/" + Fore.LIGHTYELLOW_EX + "<day>" + Fore.LIGHTCYAN_EX + "/input\"" + Fore.RESET + " " + Fore.LIGHTBLACK_EX + "(if the website uses a different format than default, change line 14 in src/interface.py to reflect it)" + Fore.RESET)
    print()
    print("You can request a single day setting " + Fore.LIGHTWHITE_EX + "Day(s)" + Fore.RESET + " to a number (es. " + Fore.LIGHTCYAN_EX + "\"1\"" + Fore.RESET + ", " + Fore.LIGHTCYAN_EX + "\"14\"" + Fore.RESET + ", " + Fore.LIGHTCYAN_EX + "\"19\"" + Fore.RESET + "), or multiple days using the format " + Fore.LIGHTCYAN_EX + "\"" + Fore.LIGHTYELLOW_EX + "<first day>" + Fore.LIGHTCYAN_EX + "-" + Fore.LIGHTYELLOW_EX + "<last day>" + Fore.LIGHTCYAN_EX + "\"" + Fore.RESET)
    print("If you request multiple days it might take, a while before the inputs will be downloaded (between each request there's a sleep of 4 minutes). So be patient.")
    print("If you have " + Fore.LIGHTBLUE_EX + "\"AOC_API\"" + Fore.RESET + " set, you have to confirm that you want to use it as API Website, by typing " + Fore.LIGHTGREEN_EX + "Y" + Fore.RESET + " when asked")
    print("If you don't know how to obtain your " + Fore.LIGHTWHITE_EX + "Session Token" + Fore.RESET + " check the " + Fore.LIGHTGREEN_EX + "How to get your session token" + Fore.RESET + " section in the " + Fore.LIGHTCYAN_EX + "README.md" + Fore.RESET + " file or go to https://github.com/gdar463/aoc-getter#How-to-get-your-session-token")
    print()
    print("After this line there'll be all the inputs.")
    print()
