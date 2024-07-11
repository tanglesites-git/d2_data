from json import dumps


def create_plug_set_item(x):
    return x.get('plugItemHash')


class PlugSetTypeDto:

    def __init__(self, reusablePlugItems: list[dict[str, int]]):
        self.reusablePlugItems = [create_plug_set_item(x) for x in reusablePlugItems]

    @classmethod
    def From(cls, data: dict[str, any]) -> 'PlugSetTypeDto':
        return cls(
            data.get('reusablePlugItems')
        )

    def __dict__(self) -> dict[str, any]:
        return {
            'reusablePlugItems': self.reusablePlugItems
        }

    def __repr__(self) -> str:
        return dumps(self.__dict__(), indent=2)

    def __str__(self) -> str:
        return dumps(self.__dict__())