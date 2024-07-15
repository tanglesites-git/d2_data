from pathlib import Path


class Files:
    Root = Path(__file__).parent.parent
    ManifestJson = Root / 'data' / 'manifest.json'
    WeaponsJson = Root / 'data' / 'weapons.json'
    DestinyCollectibleDefinitionJson = Root / 'data' / 'Definitions' / 'DestinyCollectibleDefinition.json'
    DestinyDamageTypeDefinitionJson = Root / 'data' / 'Definitions' / 'DestinyDamageTypeDefinition.json'
    DestinyEquipmentSlotDefinitionJson = Root / 'data' / 'Definitions' / 'DestinyEquipmentSlotDefinition.json'
    DestinyInventoryItemDefinitionJson = Root / 'data' / 'Definitions' / 'DestinyInventoryItemDefinition.json'
    DestinyLoreDefinitionJson = Root / 'data' / 'Definitions' / 'DestinyLoreDefinition.json'
    DestinyPlugSetDefinitionJson = Root / 'data' / 'Definitions' / 'DestinyPlugSetDefinition.json'
    DestinySocketCategoryDefinitionJson = Root / 'data' / 'Definitions' / 'DestinySocketCategoryDefinition.json'
    DestinyStatDefinitionJson = Root / 'data' / 'Definitions' / 'DestinyStatDefinition.json'
    DestinyFileDefinitions = [
        str(DestinyCollectibleDefinitionJson),
        str(DestinyDamageTypeDefinitionJson),
        str(DestinyEquipmentSlotDefinitionJson),
        str(DestinyInventoryItemDefinitionJson),
        str(DestinyLoreDefinitionJson),
        str(DestinyPlugSetDefinitionJson),
        str(DestinySocketCategoryDefinitionJson),
        str(DestinyStatDefinitionJson),
    ]
