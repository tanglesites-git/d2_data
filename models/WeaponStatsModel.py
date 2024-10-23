class WeaponStatsModel:

    def __init__(self, id, stat_id, value):
        self._id = id
        self._stat_id = stat_id
        self._value = value

    @property
    def id(self):
        return self._id

    @property
    def stat_id(self):
        return self._stat_id

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, data):
        self._value = data

    @id.setter
    def weapon_id(self, value):
        self._id = value

    @stat_id.setter
    def stat_id(self, value):
        self._stat_id = value

    @classmethod
    def from_dict(cls, data):
        return WeaponStatsModel(data['hash'], data['stathash'], data['value'])

    def __eq__(self, other):
        if not isinstance(other, WeaponStatsModel):
            return NotImplemented
        return self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if not isinstance(other, WeaponStatsModel):
            return NotImplemented
        return self.id < other.id

    def __gt__(self, other):
        if not isinstance(other, WeaponStatsModel):
            return NotImplemented
        return self.id > other.id