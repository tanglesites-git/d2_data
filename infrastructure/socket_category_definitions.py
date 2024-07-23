from json import load

from utils import write_to_excel, write_to_json
from kernel import DataDirectory


def parse_socket_category_definitions():
    dictionary = {
        "description": [],
        "name": [],
        "hash": [],
    }

    with open(DataDirectory / "DestinySocketCategoryDefinition.json", "r") as f:
        data = load(f)

        for key, value in data.items():

            dictionary["description"].append(value["displayProperties"]["description"])
            dictionary["name"].append(value["displayProperties"]["name"])
            dictionary["hash"].append(value["hash"])

        write_to_json(dictionary, "DestinySocketCategoryDefinition.json")
        write_to_excel(dictionary, "DestinySocketCategoryDefinition.xlsx")


if __name__ == '__main__':
    pass
