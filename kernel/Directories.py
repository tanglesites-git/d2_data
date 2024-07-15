from pathlib import Path


class Dir:
    Root = Path(__file__).parent.parent
    Data = Root / 'data'
    DestinyInventoryItemDefinitionDir = Data / 'DestinyInventoryItemDefinition'
    Definitions = Data / 'Definitions'

    @staticmethod
    def create_dirs():
        Dir.Root.mkdir(exist_ok=True, parents=True)
        Dir.Data.mkdir(exist_ok=True, parents=True)
        Dir.DestinyInventoryItemDefinitionDir.mkdir(exist_ok=True, parents=True)
        Dir.Definitions.mkdir(exist_ok=True, parents=True)

