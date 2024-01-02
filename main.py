import platform

# noinspection PyBroadException
try:
    from colorama import just_fix_windows_console
except Exception as e:
    import sys
    sys.exit("Before running this file you have to run \"pip install -r requirements.txt\"")

import src.env_var as env_var
import src.init_message as init_message
import src.inputs as inputs
import src.interface as interface

if platform.system() == "Windows":
    just_fix_windows_console()

init_message.init_message()

year = inputs.get_year()
days = inputs.get_days()
token = env_var.get_token()
api_server = env_var.get_api_server()

bodies: list[str] | str
if type(days) is list:
    interface.get_inputs(year, days, token, api_server)
else:
    interface.get_input(year, days, token, api_server)
