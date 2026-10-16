from dataclasses import dataclass


@dataclass
class ValidationRespose():
    data: dict | None = None
    syntax = bool | None = None
    in_DB = bool | None = None


def validate(data) -> object:
    response = ValidationRespose()

    response.data = data
