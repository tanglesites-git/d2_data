from pathlib import Path


class DirectoryPaths:
    Root = Path(__file__).parent.parent
    Data = Root / 'data'
    DestinyInventoryItemDefinition = Data / 'DestinyInventoryItemDefinition'
    DestinyStatDefinition = Data / 'DestinyStatDefinition'
    DestinyDamageTypeDefinition = Data / 'DestinyDamageTypeDefinition'
    DestinySlotTypeDefinition = Data / 'DestinySlotTypeDefinition'
    DestinyEquipmentSlotDefinition = Data / 'DestinyEquipmentSlotDefinition'
    DestinyLoreDefinition = Data / 'DestinyLoreDefinition'
    DestinyPlugSetDefinition = Data / 'DestinyPlugSetDefinition'

    @classmethod
    def does_exists(self, dir_name: Path):
        return dir_name.exists()

    @classmethod
    def create_data_directory(self, dir_name: Path):
        if self.does_exists(dir_name) is False:
            dir_name.mkdir(exist_ok=True)
        return self

