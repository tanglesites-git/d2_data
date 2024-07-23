from json import load

from utils import write_to_excel, write_to_json
from kernel import DataDirectory


def parse_damage_type_definitions():
    dictionary = {
        "description": [],
        "name": [],
        "icon": [],
        "hash": [],
        "transparentIconPath": [],
        "red": [],
        "green": [],
        "blue": [],
        "alpha": [],
    }

    with open(DataDirectory / "DestinyDamageTypeDefinition.json", "r", encoding="utf-8") as f:
        data = load(f)

        for key, value in data.items():

            if "color" not in value:
                continue

            description = value["displayProperties"]["description"]
            name = value["displayProperties"]["name"]
            if "icon" in value["displayProperties"]:
                icon = value["displayProperties"]["icon"]
            else:
                icon = ""
            hash = value["hash"]

            if "transparentIconPath" in value["displayProperties"]:
                transparentIconPath = value["transparentIconPath"]
            else:
                transparentIconPath = ""

            red = value["color"]["red"]
            green = value["color"]["green"]
            blue = value["color"]["blue"]
            alpha = value["color"]["alpha"]

            dictionary["description"].append(description)
            dictionary["name"].append(name)
            dictionary["icon"].append(icon)
            dictionary["hash"].append(hash)
            dictionary["transparentIconPath"].append(transparentIconPath)
            dictionary["red"].append(red)
            dictionary["green"].append(green)
            dictionary["blue"].append(blue)
            dictionary["alpha"].append(alpha)

    write_to_json(dictionary, "DestinyDamageTypeDefinition.json")
    write_to_excel(dictionary, "DestinyDamageTypeDefinition.xlsx")


if __name__ == '__main__':
    pass