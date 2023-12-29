import os
import pathlib
import re
from exceptions import Inputs, InputNotFormattedCorrectlyException


def parseDays(stuff: str):
    start = int(re.findall(r"^(\d\d|\d)", stuff)[0])
    end = int(re.findall(r"(\d\d|\d)$", stuff)[0])
    return [i + start for i in range(end - start + 1)]


year = input("Year (4-digit): ")
if re.match(r"^\d\d\d\d$", year) is None:
    raise InputNotFormattedCorrectlyException(Inputs.YEAR, year)

inputDays = input("Day(s) (single or in <start>-<end> format): ")
days: list[int] | int
if re.match(r"^(\d|\d\d)-(\d|\d\d)$", inputDays) is not None:
    days = parseDays(inputDays)
else:
    if re.match(r"^(\d\d|\d)$", inputDays) is not None:
        days = int(inputDays)
    else:
        raise InputNotFormattedCorrectlyException(Inputs.DAYS, inputDays)


