import argparse

parser = argparse.ArgumentParser()

parser.add_argument('action')
parser.add_argument('--description')
parser.add_argument('--amount')


def get_args():
    return parser.parse_args()
