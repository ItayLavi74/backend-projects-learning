import argparse

parser = argparse.ArgumentParser()

parser.add_argument('action')
parser.add_argument('--id')
parser.add_argument('--description')
parser.add_argument('--amount')
parser.add_argument('--month')


def get_args():
    return parser.parse_args()
