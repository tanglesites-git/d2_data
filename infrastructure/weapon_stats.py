from json import load

from kernel import DataDirectory
from utils import write_to_json, write_to_excel


def parse_weapon_stats():
    dictionary = {
        "weapon_id": [],
        "stat_id": [],
        "value": []
    }

    with open(DataDirectory / "DestinyInventoryItemDefinition.json", "r") as f:
        data = load(f)

        for key, value in data.items():

            if value["itemType"] != 3:
                continue

            if "stats" not in value:
                continue

            dictionary["weapon_id"].append(value["hash"])
            stat_list = []
            value_list = []

            for stat_key, stat_value in value["stats"]["stats"].items():
                stat_list.append(stat_key)
                value_list.append(stat_value["value"])
            dictionary["stat_id"].append(stat_list)
            dictionary["value"].append(value_list)

    write_to_json(dictionary, "WeaponStatsDefinition.json")
    write_to_excel(dictionary, "WeaponStatsDefinition.xlsx")
