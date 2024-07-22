from json import load

from infrastructure import write_to_excel, write_to_json
from kernel import DataDirectory


def parse_collectible_definitions():
    dictionary = {
        "name": [],
        "icon": [],
        "hash": [],
        "sourceString": []
    }

    with open(DataDirectory / "DestinyCollectibleDefinition.json", "r", encoding="utf-8") as f:
        data = load(f)

        for key, value in data.items():
            name = value["displayProperties"]["name"]

            if "icon" in value["displayProperties"]:
                icon = value["displayProperties"]["icon"]
            else:
                icon = ""
            hash = value["hash"]
            if "sourceString" in value:
                sourceString = value["sourceString"]
            else:
                sourceString = ""

            dictionary["name"].append(name)
            dictionary["icon"].append(icon)
            dictionary["hash"].append(hash)
            dictionary["sourceString"].append(sourceString)
    write_to_json(dictionary, "DestinyCollectibleDefinition.json")
    write_to_excel(dictionary, "DestinyCollectibleDefinition.xlsx")


if __name__ == '__main__':
    pass
