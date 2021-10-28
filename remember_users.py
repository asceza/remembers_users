import json

filename = "data.json"


def get_data_from_file():
    try:
        with open(filename) as f:
            name = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return name


def set_data_to_file():
    name = input("Ваше имя не найдено в файле\nВведите его пожалуйста ")
    with open(filename, "w") as f:
        json.dump(name, f)
        print("Ваше имя добавлено в файл")
        return name


def print_greetings():
    name = get_data_from_file()
    if name:
        print(f"Hello {name}")
    else:
        name = set_data_to_file()
        print(f"Hello {name}")


if __name__ == "__main__":
    print_greetings()
