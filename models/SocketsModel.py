class SocketsModel:
    def __init__(self, id, name, description, displayname, tiertype, icon):
        self._id = id
        self._name = name
        self._description = description
        self._displayname = displayname
        self._tiertype = tiertype
        self._icon = icon

    # Property for id
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    # Property for name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # Property for description
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    # Property for displayname
    @property
    def displayname(self):
        return self._displayname

    @displayname.setter
    def displayname(self, value):
        self._displayname = value

    # Property for tiertype
    @property
    def tiertype(self):
        return self._tiertype

    @tiertype.setter
    def tiertype(self, value):
        self._tiertype = value

    # Property for icon
    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value

    # Class method for creating an instance from a dictionary
    @classmethod
    def from_dict(cls, data) -> 'SocketsModel':
        return cls(
            id=data.get('hash'),
            name=data.get('name'),
            description=data.get('description'),
            displayname=data.get('displayname'),
            tiertype=data.get('tiertype'),
            icon=data.get('icon')
        )

    # Override __eq__ for equality
    def __eq__(self, other):
        if not isinstance(other, SocketsModel):
            return NotImplemented
        return self.id == other.id

    # Override __ne__ for not-equal
    def __ne__(self, other):
        return not self.__eq__(other)

    # Override __lt__ for less-than
    def __lt__(self, other):
        if not isinstance(other, SocketsModel):
            return NotImplemented
        return self.id < other.id

    # Override __gt__ for greater-than
    def __gt__(self, other):
        if not isinstance(other, SocketsModel):
            return NotImplemented
        return self.id > other.id

    # Override __dict__ to return a dictionary representation of the object
    def __dict__(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'displayname': self.displayname,
            'tiertype': self.tiertype,
            'icon': self.icon
        }

    def to_dict(self):
        return self.__dict__
