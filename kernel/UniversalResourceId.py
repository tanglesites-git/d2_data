from application.dtos.JsonWorldComponentContentPaths import JsonWorldComponentContentPaths


class URI:
    BaseUrl = 'https://www.bungie.net/'
    Manifest = f'{BaseUrl}/Platform/Destiny2/Manifest'
    JsonWorldComponentContentPaths = []

    @classmethod
    def init_JsonWorldComponentContentPaths(cls, manifest: dict):
        json_world_component_content_paths = JsonWorldComponentContentPaths.From(manifest['Response']['jsonWorldComponentContentPaths'])
        english = json_world_component_content_paths.en

        table_urls = (
            english.DestinyInventoryItemDefinition,
            english.DestinyDamageTypeDefinition,
            english.DestinyLoreDefinition,
            english.DestinyStatDefinition,
            english.DestinyPlugSetDefinition,
            english.DestinyEquipmentSlotDefinition,
            english.DestinyCollectibleDefinition,
            english.DestinySocketCategoryDefinition,
        )

        table_names = (
            'DestinyInventoryItemDefinition',
            'DestinyDamageTypeDefinition',
            'DestinyLoreDefinition',
            'DestinyStatDefinition',
            'DestinyPlugSetDefinition',
            'DestinyEquipmentSlotDefinition',
            'DestinyCollectibleDefinition',
            'DestinySocketCategoryDefinition',
        )

        return table_names, table_urls
