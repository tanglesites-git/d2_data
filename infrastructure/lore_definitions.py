from json import load

from kernel import DataDirectory
from utils import write_to_json, write_to_excel


def parse_lore_definitions():
    dictionary = {
        "hash": [],
        "description": [],
        "name": [],
        "subtitle": [],
    }

    with open(DataDirectory / "DestinyLoreDefinition.json", "r") as f:
        data = load(f)

        for key, value in data.items():

            if "subtitle" in value:
                dictionary["subtitle"].append(value["subtitle"])
            else:
                dictionary["subtitle"].append("")

            dictionary["description"].append(value["displayProperties"]["description"])
            dictionary["name"].append(value["displayProperties"]["name"])
            dictionary["hash"].append(value["hash"])

    write_to_json(dictionary, "DestinyLoreDefinition.json")
    write_to_excel(dictionary, "DestinyLoreDefinition.xlsx")
