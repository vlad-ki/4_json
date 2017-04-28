import json
from sys import argv


def main():
    filepath = argv[1]
    data = load_data(filepath)
    pretty_print_json(data)


def load_data(filepath):
    with open(filepath) as fh:
        json_file = json.load(fh)
        return json_file


def pretty_print_json(data):
    print(json.dumps(data, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    main()
