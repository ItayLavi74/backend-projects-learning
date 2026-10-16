from dataclasses import dataclass, field
from email_validator import validate_email
import string

REGISTER_JSON_KEYS = ['name', 'email', 'password']


@dataclass
class ValidationResponse():
    data: dict | None = None
    syntax: bool | None = None
    in_DB: bool | None = None
    errors: list[str] = field(default_factory=list)
    ok: bool | None = None


def validate_register(data) -> ValidationResponse:
    response = ValidationResponse()

    response.data = data
    response.syntax = check_register_syntax(response)
    response.in_DB = True
    response.ok = response.syntax and response.in_DB

    return response


def check_register_syntax(response: ValidationResponse) -> bool:
    flag = True

    if not validate_keys(response):
        flag = False

    if not check_name(response):
        flag = False

    if not check_email(response):
        flag = False

    if not check_password(response):
        flag = False

    return flag


def validate_keys(response) -> bool:
    received_keys = list(response.data.keys())

    if received_keys != REGISTER_JSON_KEYS:
        response.errors.append(
            f'keys problem, keys should match to: {REGISTER_JSON_KEYS}')
        return False
    return True


def check_name(response) -> bool:
    name = response.data['name']
    allowed_chars = set(string.ascii_letters + ' ')

    if set(name) <= allowed_chars:
        return True

    response.errors.append('invalid name, name has to contain letters only')
    return False


def check_password(response) -> bool:
    password = response.data['password']
    allowed_chars = set(string.ascii_letters + string.digits)

    if set(password) <= allowed_chars:
        return True

    response.errors.append(
        'invalid password, password can only contain letter and digits')
    return False


def check_email(response) -> bool:
    email = response.data['email']
    try:
        validate_email(email)
        return True
    except:
        response.errors.append('invalid email')
        return False
