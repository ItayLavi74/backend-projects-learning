'''
This file is dedicated for functions that
check if the input that provided by the user is valid
'''

def is_valid_amount(amount) -> bool:
    return amount >= 0


def is_valid_month(month) -> bool:
    return 1 <= month <= 12


def is_valid_id(id, max) -> bool:
    return 1 <= id < max


def is_arg_provided(value):
    return value is not None
