import re

from src.exceptions import InputNotFormattedCorrectlyException, Inputs, InvalidInputException, custom_raise


def parse_days(stuff: str) -> list[str]:
    start = int(re.findall(r"^(\d\d|\d)", stuff)[0])
    end = int(re.findall(r"(\d\d|\d)$", stuff)[0])
    return [str(i + start) for i in range(end - start + 1)]


def get_year() -> str:
    year = input("Year: ")
    if re.match(r"^\d\d\d\d$", year) is None:
        custom_raise(InputNotFormattedCorrectlyException, Inputs.YEAR, year)
    if not int(year) >= 2015:
        custom_raise(InvalidInputException, Inputs.YEAR, year)
    return year


def get_days() -> list[str] | str:
    inputDays = input("Day(s): ")
    days: list[str] | str
    if re.match(r"^(\d\d|\d)-(\d\d|\d)$", inputDays) is not None:
        if not (1 <= int(re.findall(r"^(\d\d|\d)", inputDays)[0]) < int(re.findall(r"(\d\d|\d)$", inputDays)[0]) and int(re.findall(r"^(\d\d|\d)", inputDays)[0]) < int(re.findall(r"(\d\d|\d)$", inputDays)[0]) <= 25):
            custom_raise(InvalidInputException, Inputs.DAYS, inputDays)
        days = parse_days(inputDays)
    else:
        if re.match(r"^(\d\d|\d)$", inputDays) is not None:
            if not (1 <= int(inputDays) <= 25):
                custom_raise(InputNotFormattedCorrectlyException, Inputs.DAYS, inputDays)
            days = inputDays
        else:
            custom_raise(InputNotFormattedCorrectlyException, Inputs.DAYS, inputDays)
    return days
