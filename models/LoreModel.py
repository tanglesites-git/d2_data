class LoreModel:

    def __init__(self, id: int, description: str, subtitle: str):
        self._id = id
        self._description = description
        self._subtitle = subtitle

    @property
    def id(self):
        return self._id

    @property
    def description(self):
        return self._description

    @property
    def subtitle(self):
        return self._subtitle

    @id.setter
    def id(self, value):
        self._id = value

    @description.setter
    def description(self, value):
        self._description = value

    @subtitle.setter
    def subtitle(self, value):
        self._subtitle = value

    @classmethod
    def from_dict(cls, data):
        return LoreModel(data['hash'], data['description'], data['subtitle'])

    def to_dict(self) -> dict:
        return self.__dict__

    def __eq__(self, other: 'LoreModel') -> bool:
        return self._id == other._id

    def __ne__(self, other: 'LoreModel') -> bool:
        return self._id != other._id

    def lt__(self, other: 'LoreModel') -> bool:
        return self._id < other._id

    def gt__(self, other: 'LoreModel') -> bool:
        return self._id > other._id