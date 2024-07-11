from json import dumps
from typing import Union

from application.dto.WeaponDto import WeaponDto


class SocketEntry:

    def __init__(self, curratedRoll: int, plugSetHash: int):
        self.curratedRoll = curratedRoll
        self.plugSetHash = plugSetHash

    @classmethod
    def From(cls, value: dict):
        return cls(value['singleInitialItemHash'], value['plugSetHash'])

    def __dict__(self):
        return {
            'curratedRoll': self.curratedRoll,
            'plugSetHash': self.plugSetHash
        }

    def __str__(self):
        return dumps(self.__dict__())

    def __repr__(self):
        return dumps(self.__dict__(), indent=4)


class StatItem:
    def __init__(self, statHash: int, value: int):
        self.statHash = statHash
        self.name = None
        self.value = value

    @classmethod
    def From(cls, value: dict):
        return cls(value['statHash'], value['value'])

    def __dict__(self):
        return {
            'statHash': self.statHash,
            'value': self.value,
            'name': self.name
        }

    def __str__(self):
        return dumps(self.__dict__())

    def __repr__(self):
        return dumps(self.__dict__(), indent=4)


class WeaponAggregate:

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
        self.screensohot = screensohot
        self.itemTypeDisplayName = itemTypeDisplayName
        self.flavorText = flavorText
        self.tierTypeName = tierTypeName
        self.stats = [StatItem.From(x[1]) for x in stats.items()]
        self.equipmentSlotTypeHash = equipmentSlotTypeHash
        self.ammoType = ammoType
        self.socketEntries = [SocketEntry.From(x) for x in socketEntries]
        self.socketCategories = socketCategories
        self.loreHash = loreHash
        self.itemType = itemType
        self.defaultDamageTypeHash = defaultDamageTypeHash

    @classmethod
    def From(cls, value: WeaponDto):
        return WeaponAggregate(
            value.hash,
            value.name,
            value.icon,
            value.iconWatermark,
            value.screenshot,
            value.itemTypeDisplayName,
            value.flavorText,
            value.tierTypeName,
            value.stats,
            value.equipmentSlotTypeHash,
            value.ammoType,
            value.socketEntries,
            value.socketCategories,
            value.loreHash,
            value.itemType,
            value.defaultDamageTypeHash
        )

    def __dict__(self):
        return {
            'hash': self.hash,
            'name': self.name,
            'icon': self.icon,
            'iconWatermark': self.iconWatermark,
            'screensohot': self.screensohot,
            'itemTypeDisplayName': self.itemTypeDisplayName,
            'flavorText': self.flavorText,
            'tierTypeName': self.tierTypeName,
            'stats': [x.__dict__() for x in self.stats],
            'equipmentSlotTypeHash': self.equipmentSlotTypeHash,
            'ammoType': self.ammoType,
            'socketEntries': self.socketEntries,
            'socketCategories': self.socketCategories,
            'loreHash': self.loreHash,
            'itemType': self.itemType,
            'defaultDamageTypeHash': self.defaultDamageTypeHash
        }

    def __str__(self):
        return dumps(self.__dict__())

    def __repr__(self):
        return dumps(self.__dict__(), indent=4)
