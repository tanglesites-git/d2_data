from typing import Union


class MobileGearAssetDataBases:

    def __init__(self, version: int, path: str):
        self.version = version
        self.path = path

    @classmethod
    def From(cls, data: list[dict[str, Union[str, int]]]) -> list["MobileGearAssetDataBases"]:
        return [cls(**item) for item in data]

    def as_dict(self):
        return {
            "version": self.version,
            "path": self.path
        }

    def __len__(self):
        return len(self.as_dict())
