import urllib.request
from user_input import get_input
import pprint
import json


def main():
    args = get_input()

    HTTP = f'https://api.github.com/users/{args.username}/events'

    response = urllib.request.urlopen(HTTP)
    bytes_response = response.read() # bytes
    json_response = bytes_response.decode('utf8').replace("'", '"')
    data = json.loads(json_response)
    pprint.pprint(data)


if __name__ == '__main__':
    main()
