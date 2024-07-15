def process_stats(x: dict):
    return {
        "statHash": x["statHash"],
        "value": x["value"]
    }


def process_socket_entries(x):
    return_value = {}
    if "singleInitialItemHash" in x:
        return_value["curratedRoll"] = x["singleInitialItemHash"]

    if "reusablePlugSetHash" in x:
        return_value["plugSetHash"] = x["reusablePlugSetHash"]

    if "randomizedPlugSetHash" in x:
        return_value["plugSetHash"] = x["randomizedPlugSetHash"]

    if "reusablePlugSetHash" in x or "randomizedPlugSetHash" in x:
        return return_value


class WeaponDTO:

    def __init__(self,
                 id: int,
                 name: str,
                 icon: str,
                 iconWatermarkUrl: str,
                 screenshotUrl: str,
                 displayName: str,
                 flavorText: str,
                 tierType: str,
                 slotTYpe: str,
                 ammoType: str,
                 stats: dict,
                 socketEntries: dict,
                 socketCategories: dict,
                 damageTypeId: int,
                 itemType: int):
        self.id = id
        self.name = name
        self.icon = icon
        self.iconWatermarkUrl = iconWatermarkUrl
        self.screenshotUrl = screenshotUrl
        self.displayName = displayName
        self.flavorText = flavorText
        self.tierType = tierType
        self.slotType = slotTYpe
        self.ammoType = ammoType
        self.stats = [process_stats(x) for x in stats.values()]
        self.socketEntries = [process_socket_entries(x) for x in socketEntries]
        self.socketCategories = socketCategories
        self.damageTypeId = damageTypeId
        self.itemType = itemType

    @classmethod
    def From(cls, x: dict):
        return cls(
            x["hash"],
            x['displayProperties']["name"],
            x['displayProperties']["icon"],
            x["iconWatermark"],
            x["screenshot"],
            x["itemTypeDisplayName"],
            x["flavorText"],
            x["inventory"]["tierTypeName"],
            x["equippingBlock"]["equipmentSlotTypeHash"],
            x["equippingBlock"]["ammoType"],
            x["stats"]["stats"],
            x["sockets"]["socketEntries"],
            x["sockets"]["socketCategories"],
            x["defaultDamageTypeHash"],
            x["itemType"]
        )

    def __dict__(self):
        return {
            "id": self.id,
            "name": self.name,
            "icon": self.icon,
            "iconWatermarkUrl": self.iconWatermarkUrl,
            "screenshotUrl": self.screenshotUrl,
            "displayName": self.displayName,
            "flavorText": self.flavorText,
            "tierType": self.tierType,
            "slotType": self.slotType,
            "ammoType": self.ammoType,
            "stats": self.stats,
            "socketEntries": self.socketEntries,
            "socketCategories": self.socketCategories,
            "damageTypeId": self.damageTypeId,
            "itemType": self.itemType
        }

    def __str__(self):
        return dumps(self.__dict__())

    def __repr__(self):
        return dumps(self.__dict__(), indent=4)
