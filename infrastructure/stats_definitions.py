from json import load

from infrastructure import write_to_excel, write_to_json
from kernel import DataDirectory


def parse_stat_definitions():
    """This is not the tradional way to handle stats: Normally you would create a dataframe (which is what I have done here) but I was not able to get the
    perfomance I wanted out of the pandas-dataframe so I have created a generic-dataframe/dictionary to store the data. This is not the best way to handle this
    data but it is the way that is working for me. Apache Spark offers some but I wanted to explore a non-framework approach to this problem."""
    dictionary = {
        "discription": [],
        "name": [],
        "icon": [],
        "hash": [],
    }

    with open(DataDirectory / "DestinyStatDefinition.json", "r", encoding="utf-8") as f:
        data = load(f)
        for key, value in data.items():
            if "displayProperties" not in value:
                continue
            if "description" not in value["displayProperties"] or "name" not in value["displayProperties"] or "icon" not in value["displayProperties"]:
                continue

            description = value["displayProperties"]["description"]
            name = value["displayProperties"]["name"]
            icon = value["displayProperties"]["icon"]
            hash = value["hash"]

            if description in dictionary["discription"] or description == "":
                continue

            if name in dictionary["name"] or name == "":
                continue

            if icon in dictionary["icon"] or icon == "":
                continue

            if hash in dictionary["hash"]:
                continue

            dictionary["discription"].append(value["displayProperties"]["description"])
            dictionary["name"].append(value["displayProperties"]["name"])
            dictionary["icon"].append(value["displayProperties"]["icon"])
            dictionary["hash"].append(value["hash"])
    write_to_json(dictionary, "DestinyStatDefinition")
    write_to_excel(dictionary, "DestinyStatDefinition")