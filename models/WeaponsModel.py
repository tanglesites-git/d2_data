class WeaponsModel:
    def __init__(self, id, name, displayname, tiertype, ammotype,
                 equipmentslot, damagetype_id, collectible_id, lore_id,
                 flavortext, icon, watermark, screenshot):
        self._id = id
        self._name = name
        self._displayname = displayname
        self._tiertype = tiertype
        self._ammotype = ammotype
        self._equipmentslot = equipmentslot
        self._damagetype_id = damagetype_id
        self._collectible_id = collectible_id
        self._lore_id = lore_id
        self._flavortext = flavortext
        self._icon = icon
        self._watermark = watermark
        self._screenshot = screenshot

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def displayname(self):
        return self._displayname

    @displayname.setter
    def displayname(self, value):
        self._displayname = value

    @property
    def tiertype(self):
        return self._tiertype

    @tiertype.setter
    def tiertype(self, value):
        self._tiertype = value

    @property
    def ammotype(self):
        return self._ammotype

    @ammotype.setter
    def ammotype(self, value):
        self._ammotype = value

    @property
    def equipmentslot(self):
        return self._equipmentslot

    @equipmentslot.setter
    def equipmentslot(self, value):
        self._equipmentslot = value

    @property
    def damagetype_id(self):
        return self._damagetype_id

    @damagetype_id.setter
    def damagetype_id(self, value):
        self._damagetype_id = value

    @property
    def collectible_id(self):
        return self._collectible_id

    @collectible_id.setter
    def collectible_id(self, value):
        self._collectible_id = value

    @property
    def lore_id(self):
        return self._lore_id

    @lore_id.setter
    def lore_id(self, value):
        self._lore_id = value

    @property
    def flavortext(self):
        return self._flavortext

    @flavortext.setter
    def flavortext(self, value):
        self._flavortext = value

    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value

    @property
    def watermark(self):
        return self._watermark

    @watermark.setter
    def watermark(self, value):
        self._watermark = value

    @property
    def screenshot(self):
        return self._screenshot

    @screenshot.setter
    def screenshot(self, value):
        self._screenshot = value

    @classmethod
    def from_dict(cls, data) -> 'WeaponsModel':
        return cls(
            id=data.get('id'),
            name=data.get('name'),
            displayname=data.get('displayname'),
            tiertype=data.get('tiertype'),
            ammotype=data.get('ammotype'),
            equipmentslot=data.get('equipmentslot'),
            damagetype_id=data.get('damagetype_id'),
            collectible_id=data.get('collectible_id'),
            lore_id=data.get('lore_id'),
            flavortext=data.get('flavortext'),
            icon=data.get('icon'),
            watermark=data.get('watermark'),
            screenshot=data.get('screenshot')
        )

    def to_dict(self):
        return self.__dict__

    def __eq__(self, other):
        if not isinstance(other, WeaponsModel):
            return NotImplemented
        return self._id == other._id

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if not isinstance(other, WeaponsModel):
            return NotImplemented
        return self._id < other._id

    def __gt__(self, other):
        if not isinstance(other, WeaponsModel):
            return NotImplemented
        return self._id > other._id