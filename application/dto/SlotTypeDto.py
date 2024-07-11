from json import dumps


class SlotTypeDto:

    def __init__(self, hash: int, name: str, description: str):
        self.hash = hash
        self.name = name
        self.description = description

    @classmethod
    def From(cls, value: dict):
        return cls(value["hash"], value["displayProperties"]["name"], value["displayProperties"]["description"])

    def __dict__(self):
        return {
            "hash": self.hash,
            "name": self.name,
            "description": self.description
        }

    def __str__(self):
        return dumps(self.__dict__())

    def __repr__(self):
        return dumps(self.__dict__(), indent=4)