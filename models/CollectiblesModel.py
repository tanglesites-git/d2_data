class CollectiblesModel:

    def __init__(self, id: int, sourcestring: str):
        self._id = id
        self._sourcestring = sourcestring

    @property
    def id(self):
        return self._id

    @property
    def sourcestring(self):
        return self._sourcestring

    @sourcestring.setter
    def sourcestring(self, sourcestring):
        self._sourcestring = sourcestring

    @id.setter
    def id(self, id):
        self._id = id

    @classmethod
    def from_dict(cls, dictionary: dict):
        return CollectiblesModel(dictionary['hash'], dictionary['sourcestring'])


    def to_dict(self) -> dict:
        return self.__dict__

    def __eq__(self, other: 'CollectiblesModel') -> bool:
        return self._id == other._id

    def __ne__(self, other: 'CollectiblesModel') -> bool:
        return self._id != other._id

    def lt__(self, other: 'CollectiblesModel') -> bool:
        return self._id < other._id

    def gt__(self, other: 'CollectiblesModel') -> bool:
        return self._id > other._id