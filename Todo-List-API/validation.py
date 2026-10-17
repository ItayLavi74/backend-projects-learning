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
    response.syntax = _check_register_syntax(response)
    response.in_DB = True
    response.ok = response.syntax and response.in_DB

    return response


def _check_register_syntax(response: ValidationResponse) -> bool:
    flag = True

    if not _validate_keys(response):
        flag = False

    if not _check_name(response):
        flag = False

    if not _check_email(response):
        flag = False

    if not _check_password(response):
        flag = False

    return flag


def _validate_keys(response) -> bool:
    received_keys = list(response.data.keys())

    if received_keys != REGISTER_JSON_KEYS:
        response.errors.append(
            f'keys problem, keys should match to: {REGISTER_JSON_KEYS}')
        return False
    return True


def _check_name(response) -> bool:
    name = response.data['name']

    if name == '':
        response.errors.append('invalid name, name cannot be empty')
        return False

    allowed_chars = set(string.ascii_letters + ' ')

    if set(name) <= allowed_chars:
        return True

    response.errors.append('invalid name, name has to contain letters only')
    return False


def _check_password(response) -> bool:
    password = response.data['password']

    if password == '':
        response.errors.append('invalid password, password cannot be empty')
        return False
    
    allowed_chars = set(string.ascii_letters + string.digits)

    if set(password) <= allowed_chars:
        return True

    response.errors.append(
        'invalid password, password can only contain letter and digits')
    return False


def _check_email(response) -> bool:
    email = response.data['email']

    if email == '':
        response.errors.append('invalid email, email cannot be empty')
        return False

    try:
        validate_email(email)
        return True
    except:
        response.errors.append('invalid email')
        return False
