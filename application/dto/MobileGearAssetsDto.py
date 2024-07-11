from json import dumps


class MobileGearAssetsDto:

    def __init__(self, version: int, path: str):
        self.version = version
        self.path = path

    @classmethod
    def From(cls, value: dict):
        return cls(value['version'], value['path'])

    def __str__(self):
        return f'{{"version": "{self.version}", "path": "{self.path}"}}'

    def __dict__(self):
        return {"version": self.version, "path": self.path}

    def __iter__(self):
        return iter([self.version, self.path])

    def __repr__(self):
        return dumps(self.__dict__(), indent=4)