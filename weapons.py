from concurrent.futures import ThreadPoolExecutor
from json import load, dumps, loads

from kernel import JsonDirectory, MasterDirectory


def get_lore(data1: dict, lore_data1: dict, index1: int):
    loreHash = data1["loreHash"][index1]
    if loreHash == "":
        return {}
    index_of_loreHash = lore_data1["hash"].index(loreHash)
    return {
        "id": loreHash,
        "loreName": lore_data1["name"][index_of_loreHash],
        "loreDescription": lore_data1["description"][index_of_loreHash]
    }


def get_collectibles(data1: dict, collections_data1: dict, index1: int):
    hash = data1["collectibleHash"][index1]
    if hash == 0:
        return {}
    else:
        collectible_index = collections_data1["hash"].index(hash)
        return {
            "id": hash,
            "name": collections_data1["name"][collectible_index],
            "sourceString": collections_data1["sourceString"][collectible_index],
            "icon": collections_data1["icon"][collectible_index]
        }


def get_damage_type(data1: dict, damage_data1: dict, index1: int):
    hash = data1["defaultDamageTypeHash"][index1]
    damage_index = damage_data1["hash"].index(hash)
    return {
        "id": hash,
        "name": damage_data1["name"][damage_index],
        "description": damage_data1["description"][damage_index],
        "icon": damage_data1["icon"][damage_index],
        "transparentIconPath": damage_data1["transparentIconPath"][damage_index],
        "red": damage_data1["red"][damage_index],
        "green": damage_data1["green"][damage_index],
        "blue": damage_data1["blue"][damage_index],
        "alpha": damage_data1["alpha"][damage_index]
    }


def get_stats_values(weapon_id1: int, weapon_stats_data1: dict, stats_data1: dict):
    index_of_weapon_id = weapon_stats_data1["weapon_id"].index(weapon_id1)
    stat_id_list = weapon_stats_data1["stat_id"][index_of_weapon_id]
    stat_values_list = weapon_stats_data1["value"][index_of_weapon_id]
    stats_list = []
    for stat_index, stat_id in enumerate(stat_id_list):
        index_of_stat_data = stats_data1["hash"].index(int(stat_id))
        desc = stats_data1["description"][index_of_stat_data]
        name = stats_data1["name"][index_of_stat_data]
        value = stat_values_list[stat_index]
        stats_list.append({
            "id": stat_id,
            "name": name,
            "description": desc,
            "value": value
        })
    return stats_list


def write_master_file(weapon_id: int, d: dict):
    with open(MasterDirectory / f'{weapon_id}.json', "w", encoding="utf-8") as f:
        f.write(dumps(d, indent=4))


if not MasterDirectory.exists():
    MasterDirectory.mkdir(exist_ok=True, parents=True)

stats_data_text_io_handeler = open(JsonDirectory / "DestinyStatDefinition.json", "r", encoding="utf-8")
damage_data_text_io_handeler = open(JsonDirectory / "DestinyDamageTypeDefinition.json", "r", encoding="utf-8")
collections_data_text_io_handeler = open(JsonDirectory / "DestinyCollectibleDefinition.json", "r", encoding="utf-8")
weapon_stats_text_io_handler = open(JsonDirectory / "WeaponStatsDefinition.json", "r", encoding="utf-8")
mod_values_data_text_io_handeler = open(JsonDirectory / "DestinyWeaponMods.json", "r", encoding="utf-8")
lore_data_text_io_handeler = open(JsonDirectory / "DestinyLoreDefinition.json", "r", encoding="utf-8")

stats_data = loads(stats_data_text_io_handeler.read())
damage_data = loads(damage_data_text_io_handeler.read())
collections_data = loads(collections_data_text_io_handeler.read())
weapon_stats_data = loads(weapon_stats_text_io_handler.read())
mod_values_data = loads(mod_values_data_text_io_handeler.read())
lore_data = loads(lore_data_text_io_handeler.read())

file_list = []

with open(JsonDirectory / "DestinyInventoryItemDefinition.json") as f:
    data = load(f)

    for index, weapon_id in enumerate(data["hash"]):
        dictionary = {}

        lore_dict = get_lore(data, lore_data, index)
        collectible_dict = get_collectibles(data, collections_data, index)
        damage_dict = get_damage_type(data, damage_data, index)
        list_of_stat_objects = get_stats_values(weapon_id, weapon_stats_data, stats_data)

        dictionary["id"] = weapon_id
        dictionary["name"] = data["name"][index]
        dictionary["icon"] = data["icon"][index]
        dictionary["itemTypeDisplayName"] = data["itemTypeDisplayName"][index]
        dictionary["tierTypeName"] = data["tierTypeName"][index]
        dictionary["iconWatermark"] = data["iconWatermark"][index]
        dictionary["screenshot"] = data["screenshot"][index]
        dictionary["lore"] = lore_dict
        dictionary["flavorText"] = data["flavorText"][index]
        dictionary["collectibleHash"] = collectible_dict
        dictionary["defaultDamageTypeHash"] = damage_dict
        dictionary["stats"] = list_of_stat_objects

        file_list.append((index, dictionary))

stats_data_text_io_handeler.close()
damage_data_text_io_handeler.close()
collections_data_text_io_handeler.close()
weapon_stats_text_io_handler.close()
mod_values_data_text_io_handeler.close()
lore_data_text_io_handeler.close()

args = ((x[0], x[1]) for x in file_list)
with ThreadPoolExecutor() as executor:
    executor.map(lambda x: write_master_file(x[0], x[1]), args)

if __name__ == "__main__":
    pass
