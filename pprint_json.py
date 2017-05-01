import json
from os.path import exists
from sys import argv


def main():
    filepath = argv[1]
    json_object = load_data(filepath)
    pretty_print_json(json_object)


def load_data(filepath):
    if not exists(filepath):
        return None
    with open(filepath) as file_handler:
        json_object = json.load(file_handler)
        return json_object


def pretty_print_json(data):
    print(json.dumps(data, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    main()
