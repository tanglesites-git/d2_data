class StatModel:

    def __init__(self, id: int, name: str, description: str) -> None:
        self._id = id
        self._name = name
        self._description = description

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


    @classmethod
    def from_dict(cls, data: dict) -> 'StatModel':
        return StatModel(data['hash'], data['name'], data['description'])

    def to_dict(self) -> dict:
        return self.__dict__

    def __eq__(self, other: 'StatModel') -> bool:
        return self._id == other._id

    def __ne__(self, other: 'StatModel') -> bool:
        return self._id != other._id

    def lt__(self, other: 'StatModel') -> bool:
        return self._id < other._id

    def gt__(self, other: 'StatModel') -> bool:
        return self._id > other._id