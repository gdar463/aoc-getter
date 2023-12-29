import enum


class Inputs(enum.StrEnum):
    YEAR = "Year"
    DAYS = "Days"


class InputNotFormattedCorrectlyException(Exception):
    def __init__(self, item: Inputs, error: str):
        message = "The input \"" + error + "\" isn't formatted correctly for " + str(item.value)
        super().__init__(message)
