from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('username')


def get_input():
    return parser.parse_args()
