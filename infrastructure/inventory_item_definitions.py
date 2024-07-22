from json import load

from infrastructure import write_to_json, write_to_excel
from kernel import DataDirectory


def is_weapon(value: dict) -> bool:
    return value["itemType"] == 3


def parse_inventory_item_definitions():
    dictionary = {
        "itemTypeDisplayName": [],
        "name": [],
        "icon": [],
        "hash": [],
        "tierTypeName": [],
        "iconWatermark": [],
        "screenshot": [],
        "loreHash": [],
        "flavorText": [],
        "collectibleHash": [],
        "ammoType": [],
        "defaultDamageTypeHash": [],
    }

    with open(DataDirectory / "DestinyInventoryItemDefinition.json", "r", encoding="utf-8") as f:
        data = load(f)

        for key, value in data.items():

            if is_weapon(value) is False:
                continue

            itemTypeDisplayName = value["itemTypeDisplayName"]
            name = value["displayProperties"]["name"]
            icon = value["displayProperties"]["icon"]
            tierTypeName = value["inventory"]["tierTypeName"]
            hash = value["hash"]
            iconWatermark = value["iconWatermark"]
            screenshot = value["screenshot"]
            flavorText = value["flavorText"]
            ammoType = value["equippingBlock"]["ammoType"]
            defaultDamageTypeHash = value["defaultDamageTypeHash"]
            if "collectibleHash" in value:
                collectibleHash = value["collectibleHash"]
            else:
                collectibleHash = 0
            if "loreHash" in value:
                loreHash = value["loreHash"]
            else:
                loreHash = ""

            dictionary["hash"].append(hash)
            dictionary["name"].append(name)
            dictionary["icon"].append(icon)
            dictionary["itemTypeDisplayName"].append(itemTypeDisplayName)
            dictionary["tierTypeName"].append(tierTypeName)
            dictionary["iconWatermark"].append(iconWatermark)
            dictionary["screenshot"].append(screenshot)
            dictionary["flavorText"].append(flavorText)
            dictionary["collectibleHash"].append(collectibleHash)
            dictionary["loreHash"].append(loreHash)
            dictionary["ammoType"].append(ammoType)
            dictionary["defaultDamageTypeHash"].append(defaultDamageTypeHash)

        write_to_json(dictionary, "DestinyInventoryItemDefinition.json")
        write_to_excel(dictionary, "DestinyInventoryItemDefinition.xlsx")


if __name__ == '__main__':
    pass
