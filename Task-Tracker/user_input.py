import argparse

parser = argparse.ArgumentParser()

parser.add_argument("prog")
parser.add_argument("func")
parser.add_argument("task", type=str, nargs='?')
parser.add_argument("new_description", type=str, nargs='?')


def get_args():
    return parser.parse_args()
