from json import dumps


class MobileGearDto:

    def __init__(self, Geometry: str, Texture: str, PlateRegion: str, Gear: str, Shader: str):
        self.Geometry = Geometry
        self.Texture = Texture
        self.PlateRegion = PlateRegion
        self.Gear = Gear
        self.Shader = Shader

    @classmethod
    def From(cls, value: dict):
        return cls(value['Geometry'], value['Texture'], value['PlateRegion'], value['Gear'], value['Shader'])

    def __dict__(self):
        return {"Geometry": self.Geometry, "Texture": self.Texture, "PlateRegion": self.PlateRegion, "Gear": self.Gear, "Shader": self.Shader}

    def __str__(self):
        return dumps(self.__dict__())

    def __iter__(self):
        return iter([self.Geometry, self.Texture, self.PlateRegion, self.Gear, self.Shader])

    def __repr__(self):
        return dumps(self.__dict__(), indent=4)