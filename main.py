import platform

# noinspection PyBroadException
try:
    from colorama import just_fix_windows_console
except Exception as e:
    import sys
    sys.exit("Before running this file you have to run \"pip install -r requirements.txt\"")

import env_var
from init_message import init_message
import inputs
import interface
import saver

if platform.system() == "Windows":
    just_fix_windows_console()

init_message()

year = inputs.get_year()
days = inputs.get_days()
token = env_var.get_token()
download_path = env_var.get_download_path()
api_server = env_var.get_api_server()

bodies: list[str] | str
if type(days) is list:
    bodies = interface.get_inputs(year, days, token, api_server)
else:
    bodies = interface.get_input(year, days, token, api_server)

if type(bodies) is list:
    saver.save_files(year, days, download_path, bodies)
else:
    saver.save_file(year, days, download_path, bodies)