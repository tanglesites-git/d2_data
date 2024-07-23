import bisect
from json import load

from kernel import DataDirectory, JsonDirectory
from utils import write_to_json, write_to_excel


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1


def parse_weapon_mods():

    dictionary = {
        "weapon_id": [],
        "mod_id": [],
    }

    with open(JsonDirectory / "DestinyPlugSetDefinition.json", "r") as ff:
        plug_set_data = load(ff)
        with open(DataDirectory / "DestinyInventoryItemDefinition.json", "r") as f:
            data = load(f)

            for key, value in data.items():

                if value["itemType"] != 3:
                    continue

                entries = value["sockets"]["socketEntries"]
                weapon_id = value["hash"]
                dictionary["weapon_id"].append(weapon_id)
                mods = []
                for entry in entries:

                    if "reusablePlugSetHash" in entry:
                        plug_set_hash = entry["reusablePlugSetHash"]
                        index = plug_set_data["hash"].index(plug_set_hash)
                        # index = binary_search(ss, plug_set_hash)
                        plug_set_items = plug_set_data["plugsets"][index]
                        mods.append(plug_set_items)

                    elif "randomizedPlugSetHash" in entry:
                        plug_set_hash = entry["randomizedPlugSetHash"]
                        index = plug_set_data["hash"].index(plug_set_hash)
                        plug_set_items = plug_set_data["plugsets"][index]
                        mods.append(plug_set_items)
                    else:
                        continue
                dictionary["mod_id"].append(mods)
    write_to_json(dictionary, "DestinyWeaponMods.json")
    write_to_excel(dictionary, "DestinyWeaponMods.xlsx")






