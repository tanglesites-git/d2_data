from json import dumps


class DamageTypeDto:

    def __init__(self,
                 hash: int,
                 name: str,
                 icon: str,
                 transparentIconPath: str,
                 red: int,
                 green: int,
                 blue: int,
                 alpha: int):
        self.hash = hash
        self.name = name
        self.icon = icon
        self.transparentIconPath = transparentIconPath
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    @classmethod
    def From(cls, value: dict):
        return cls(
            value["hash"],
            value["displayProperties"]["name"],
            value["displayProperties"]["icon"] if "icon" in value else None,
            value["transparentIconPath"] if "transparentIconPath" in value else None,
            value["color"]["red"] if "color" in value else None,
            value["color"]["green"] if "color" in value else None,
            value["color"]["blue"] if "color" in value else None,
            value["color"]["alpha"] if "color" in value else None
        )

    def __dict__(self):
        return {
            "hash": self.hash,
            "name": self.name,
            "icon": self.icon,
            "transparentIconPath": self.transparentIconPath,
            "red": self.red,
            "green": self.green,
            "blue": self.blue,
            "alpha": self.alpha
        }

    def __str__(self):
        return dumps(self.__dict__())

    def __repr__(self):
        return dumps(self.__dict__(), indent=4)