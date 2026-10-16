from dataclasses import dataclass


@dataclass
class ValidationResponse():
    data: dict | None = None
    syntax: bool | None = None
    in_DB:bool | None = None


def validate(data) -> ValidationResponse:
    response = ValidationResponse()
    response.data = data

    email = data.email

    return response
