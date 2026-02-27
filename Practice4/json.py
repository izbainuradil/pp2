import json


def dict_to_json(data):
    return json.dumps(data, indent=4)


def json_to_dict(json_string):
    return json.loads(json_string)


def save_json_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def load_json_from_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)


if __name__ == "__main__":
    sample_data = {
        "name": "Nuradil",
        "age": 20,
        "city": "Almaty"
    }

    json_string = dict_to_json(sample_data)
    print(json_string)
    save_json_to_file(sample_data, "data.json")
    print(load_json_from_file("data.json"))