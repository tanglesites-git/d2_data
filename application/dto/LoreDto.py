from json import dumps


class LoreDto:

    def __init__(self, hash: int, description: str, name: str, subtitle: str):
        self.hash = hash
        self.description = description
        self.name = name
        self.subtitle = subtitle

    @classmethod
    def From(cls, value: dict):
        return cls(value["hash"], value["displayProperties"]["description"], value["displayProperties"]["name"],
                   value["subtitle"] if "subtitle" in value else None)

    def __dict__(self):
        return {
            "hash": self.hash,
            "description": self.description,
            "name": self.name,
            "subtitle": self.subtitle
        }

    def __str__(self):
        return dumps(self.__dict__())

    def __repr__(self):
        return dumps(self.__dict__(), indent=4)