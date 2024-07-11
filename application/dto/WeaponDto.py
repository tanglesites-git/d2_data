from json import dumps
from typing import Union


def to_stat_item(x):
    return {
        "hash": x[0],
        "value": x[1]["value"],
    }


def to_socket_entry(x):
    value = None
    if 'randomizedPlugSetHash' in x:
        value = x['randomizedPlugSetHash']

    if 'reusablePlugSetHash' in x:
        value = x['reusablePlugSetHash']

    return {
        "curratedRollHash": x["singleInitialItemHash"],
        "plugSetHash": value,
    }


class WeaponDto:

    def __init__(self,
                 hash: int,
                 name: str,
                 icon: str,
                 iconWatermark: str,
                 screensohot: str,
                 itemTypeDisplayName: str,
                 flavorText: str,
                 tierTypeName: str,
                 stats: dict,
                 equipmentSlotTypeHash: int,
                 ammoType: int,
                 socketEntries: list[dict],
                 socketCategories: list[dict],
                 loreHash: Union[int, None],
                 itemType: int,
                 defaultDamageTypeHash: int):
        self.hash = hash
        self.name = name
        self.icon = icon
        self.iconWatermark = iconWatermark
        self.screenshot = screensohot
        self.itemTypeDisplayName = itemTypeDisplayName
        self.flavorText = flavorText
        self.tierTypeName = tierTypeName
        self.stats = [to_stat_item(x) for x in stats.items()]
        self.equipmentSlotTypeHash = equipmentSlotTypeHash
        self.ammoType = ammoType
        self.socketEntries = [to_socket_entry(x) for x in socketEntries]
        self.socketCategories = socketCategories
        self.loreHash = loreHash if loreHash is not None else None
        self.itemType = itemType
        self.defaultDamageTypeHash = defaultDamageTypeHash

    @classmethod
    def From(cls, value: dict):
        return WeaponDto(
            value["hash"],
            value["displayProperties"]["name"],
            value["displayProperties"]["icon"],
            value["iconWatermark"],
            value["screenshot"],
            value["itemTypeDisplayName"],
            value["flavorText"],
            value["inventory"]["tierTypeName"],
            value["stats"]["stats"] ,
            value["equippingBlock"]["equipmentSlotTypeHash"],
            value["equippingBlock"]["ammoType"],
            value["sockets"]["socketEntries"],
            value["sockets"]["socketCategories"],
            value["loreHash"] if "loreHash" in value else None,
            value["itemType"],
            value["defaultDamageTypeHash"],
        )

    def __dict__(self):
        return {
            "hash": self.hash,
            "name": self.name,
            "icon": self.icon,
            "iconWatermark": self.iconWatermark,
            "screenshot": self.screenshot,
            "itemTypeDisplayName": self.itemTypeDisplayName,
            "flavorText": self.flavorText,
            "tierTypeName": self.tierTypeName,
            "stats": self.stats,
            "equipmentSlotTypeHash": self.equipmentSlotTypeHash,
            "ammoType": self.ammoType,
            "socketEntries": self.socketEntries,
            "socketCategories": self.socketCategories,
            "loreHash": self.loreHash,
            "itemType": self.itemType,
            "defaultDamageTypeHash": self.defaultDamageTypeHash,
        }

    def __str__(self):
        return dumps(self.__dict__())

    def __repr__(self):
        return dumps(self.__dict__(), indent=4)
