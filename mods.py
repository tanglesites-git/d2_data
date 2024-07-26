from json import loads, dumps

from kernel import DataDirectory, JsonDirectory, MasterDirectory

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

            if "itemCategoryHashes" in diid_data[str(mod_id)]:
                if 610365472 in diid_data[str(mod_id)]["itemCategoryHashes"]:
                    if mod_id in ss:
                        continue
                    else:
                        dictionary_item = {}
                        ss.add(mod_id)
                        dictionary["weapon_id"].append(mod_id)
                    dictionary_item["id"] = mod_id
                    dictionary_item["name"] = diid_data[str(mod_id)]["displayProperties"]["name"]
                    dictionary_item["description"] = diid_data[str(mod_id)]["displayProperties"]["description"]
                    if "icon" in diid_data[str(mod_id)]["displayProperties"]:
                        dictionary_item["icon"] = diid_data[str(mod_id)]["displayProperties"]["icon"]
                    else:
                        dictionary_item["icon"] = "None"
                    if "itemTypeDisplayName" in diid_data[str(mod_id)]:  # Some mods don't have this
                        dictionary_item["displayName"] = diid_data[str(mod_id)]["itemTypeDisplayName"]
                    else:
                        dictionary_item["displayName"] = "None"
                    if "inventory" in diid_data[str(mod_id)] and "tierTypeName" in diid_data[(str(mod_id))]["inventory"]:  # Some mods don't have this
                        dictionary_item["tierTypeName"] = diid_data[str(mod_id)]["inventory"]["tierTypeName"]
                    else:
                        dictionary_item["tierTypeName"] = "None"
                    dictionary_item["stats"] = []
                    if "investmentStats" in diid_data[str(mod_id)]:
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
                    else:
                        dictionary_item["stats"] = []

                    dictionary["mod_object"].append(dictionary_item)

with open(JsonDirectory / "Mods.json", "w", encoding='utf-8') as f:
    f.write(dumps(dictionary, indent=2))

diid_handler.close()
mods_handler.close()
stats_handler.close()

if __name__ == '__main__':
    pass
