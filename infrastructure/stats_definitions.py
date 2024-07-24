from json import load

from utils import write_to_excel, write_to_json
from kernel import DataDirectory


def parse_stat_definitions():

    dictionary = {
        "description": [],
        "name": [],
        "icon": [],
        "hash": [],
    }

    with open(DataDirectory / "DestinyStatDefinition.json", "r", encoding="utf-8") as f:
        data = load(f)

        for key, value in data.items():

            description = value["displayProperties"]["description"]
            name = value["displayProperties"]["name"]
            if "icon" in value["displayProperties"]:
                icon = value["displayProperties"]["icon"]
            else:
                icon = ""
            hash = value["hash"]

            dictionary["description"].append(description)
            dictionary["name"].append(name)
            dictionary["icon"].append(icon)
            dictionary["hash"].append(hash)

    write_to_json(dictionary, "DestinyStatDefinition.json")
    write_to_excel(dictionary, "DestinyStatDefinition.xlsx")


if __name__ == '__main__':
    parse_stat_definitions()

