class DamageTypeModel:

    def __init__(self, id: int, name: str, description: str, icon: str):
        self._id = id
        self._name = name
        self._description = description
        self._icon = icon

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
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value

    @classmethod
    def from_dict(cls, dictionary: dict) -> 'DamageTypeModel':
        return DamageTypeModel(
            dictionary['hash'],
            dictionary['name'],
            dictionary['description'],
            dictionary['icon']
        )

    def to_dict(self) -> dict:
        return self.__dict__

    def __eq__(self, other: 'DamageTypeModel') -> bool:
        return self._id == other._id

    def __ne__(self, other: 'DamageTypeModel') -> bool:
        return self._id != other._id

    def lt__(self, other: 'DamageTypeModel') -> bool:
        return self._id < other._id

    def gt__(self, other: 'DamageTypeModel') -> bool:
        return self._id > other._id