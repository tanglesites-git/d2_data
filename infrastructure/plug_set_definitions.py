from json import load

from kernel import DataDirectory, JsonDirectory
from utils import write_to_excel, write_to_json


def parse_plug_set_definitions():
    dictionary = {
        "plugsets": [],
        "hash": [],
    }

    with open(DataDirectory / "DestinyPlugSetDefinition.json", "r") as f:
        data = load(f)

        for key, value in data.items():
            dictionary["hash"].append(value["hash"])
            dictionary["plugsets"].append(
                [x["plugItemHash"] for x in value["reusablePlugItems"]]
            )

    write_to_json(dictionary, "DestinyPlugSetDefinition.json")
    write_to_excel(dictionary, "DestinyPlugSetDefinition.xlsx")

