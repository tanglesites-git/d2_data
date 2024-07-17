class MobileGearCDN:

    def __init__(self, Geometry: str, Texture: str, PlateRegion: str, Gear: str, Shader: str):
        self.Geometry = Geometry
        self.Texture = Texture
        self.PlateRegion = PlateRegion
        self.Gear = Gear
        self.Shader = Shader

    @classmethod
    def From(cls, data: dict[str, str]) -> "MobileGearCDN":
        return cls(**data)

    def as_dict(self):
        return {
            "Geometry": self.Geometry,
            "Texture": self.Texture,
            "PlateRegion": self.PlateRegion,
            "Gear": self.Gear,
            "Shader": self.Shader
        }

    def __len__(self):
        return len(self.as_dict())