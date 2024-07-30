from threading import Lock
from concurrent.futures import ThreadPoolExecutor
from json import loads, dumps
from time import perf_counter_ns

from memory_profiler import memory_usage

from kernel import DataDirectory, JsonDirectory
from utils import write_to_json, write_to_excel


lock = Lock()


def if_no_icon(diid_data=None, mod_id=None, dictionary_item=None):
    if "icon" not in diid_data[str(mod_id)]["displayProperties"]:
        dictionary_item["icon"] = "None"


def if_no_item_type_display_name(diid_data=None, mod_id=None, dictionary_item=None):
    if "itemTypeDisplayName" not in diid_data[str(mod_id)]:  # Some mods don't have this
        dictionary_item["displayName"] = "None"


def if_no_tier_type_name(diid_data=None, mod_id=None, dictionary_item=None):
    if ("inventory" not in diid_data[str(mod_id)]
            and "tierTypeName" not in diid_data[(str(mod_id))]["inventory"]):  # Some mods don't have this
        dictionary_item["tierTypeName"] = "None"


def if_no_investment_stats(diid_data=None, mod_id=None, dictionary_item=None):
    if "investmentStats" not in diid_data[str(mod_id)]:
        dictionary_item["stats"] = []


def create_mod(mod_id=None, diid_data=None, stats_data=None, dictionary_item=None):
    dictionary_item["id"] = mod_id
    dictionary_item["name"] = diid_data[str(mod_id)]["displayProperties"]["name"]
    dictionary_item["description"] = diid_data[str(mod_id)]["displayProperties"]["description"]
    dictionary_item["icon"] = diid_data[str(mod_id)]["displayProperties"]["icon"]
    dictionary_item["displayName"] = diid_data[str(mod_id)]["itemTypeDisplayName"]
    dictionary_item["tierTypeName"] = diid_data[str(mod_id)]["inventory"]["tierTypeName"]
    dictionary_item["stats"] = []

    for stats in diid_data[str(mod_id)]["investmentStats"]:
        index_of_stat_id = stats_data["hash"].index(stats["statTypeHash"])
        stat_dict = {
            "description": stats_data["description"][index_of_stat_id],
            "id": stats_data["hash"][index_of_stat_id],
            "icon": stats_data["icon"][index_of_stat_id],
            "name": stats_data["name"][index_of_stat_id],
            "value": stats["value"]
        }
        dictionary_item["stats"].append(stat_dict)


def create_mod_object(diid_data=None, mod_id=None, ss=None, dictionary_item=None, stats_data=None, dictionary=None):
    if_no_icon(diid_data, mod_id, dictionary_item)
    if_no_item_type_display_name(diid_data, mod_id, dictionary_item)
    if_no_tier_type_name(diid_data, mod_id, dictionary_item)
    if_no_investment_stats(diid_data, mod_id, dictionary_item)

    create_mod(mod_id, diid_data, stats_data, dictionary_item)

    with lock:
        dictionary["mod_object"].append(dictionary_item)


def create_mods():

    diid_handler = open(DataDirectory / "DestinyInventoryItemDefinition.json", "r", encoding='utf-8')
    mods_handler = open(JsonDirectory / "DestinyWeaponMods.json", "r", encoding='utf-8')
    stats_handler = open(JsonDirectory / "DestinyStatDefinition.json", "r", encoding='utf-8')

    diid_data = loads(diid_handler.read())
    mods_data = loads(mods_handler.read())
    stats_data = loads(stats_handler.read())

    # Code goes here
    dictionary = {
        "weapon_id": [],
        "mod_object": []
    }
    ss = set()
    for array in mods_data["mod_id"]:
        for child_array in array:

            for mod_id in child_array:
                data_list = []
                if "itemCategoryHashes" in diid_data[str(mod_id)]:
                    if 610365472 in diid_data[str(mod_id)]["itemCategoryHashes"]:
                        if mod_id in ss:
                            continue
                        else:
                            dictionary_item = {}
                            ss.add(mod_id)
                            dictionary["weapon_id"].append(mod_id)
                        data_list.append((diid_data, mod_id, ss, dictionary_item, stats_data, dictionary))

                with ThreadPoolExecutor() as executor:
                    executor.map(lambda x: create_mod_object(*x), data_list)
    write_to_json(dictionary, "Mods.json")
    # write_to_excel(dictionary, "Mods.xlsx")

    diid_handler.close()
    mods_handler.close()
    stats_handler.close()


if __name__ == '__main__':
    start = perf_counter_ns()
    mem_usage_start = memory_usage(include_children=True, multiprocess=True)
    print(f"Memory usage (Before): {mem_usage_start[0]}MiB")

    create_mods()

    mem_usage_end = memory_usage(include_children=True, multiprocess=True)
    print(f"Memory usage (After): {mem_usage_end[0]}MiB")
    end = perf_counter_ns()
    print(f"Memory usage (Difference): {mem_usage_end[0][0] - mem_usage_start[0][0]}MiB")
    print(f"Time taken: {(end - start) / 1_000_000_000}s")
