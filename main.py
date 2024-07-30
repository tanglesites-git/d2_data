import json

from kernel import DataDirectory
from utils import write_to_json, write_to_excel

item_number = 0

dictionary = {}
dictionary_excel = {}

with open(DataDirectory / "DestinyInventoryItemDefinition.json") as f:
    inventory_item_definition = json.load(f)
    print(f'Number of Items: {len(inventory_item_definition)}')

    for key, value in inventory_item_definition.items():

        if 'itemTypeDisplayName' not in value:
            continue
        itdn = value['itemTypeDisplayName']
        if itdn not in dictionary:
            dictionary[itdn] = 1
            dictionary_excel[itdn] = [1]
        else:
            dictionary[itdn] += 1
            dictionary_excel[itdn][0] += 1
        item_number += 1

    dictionary1 = dict(sorted(dictionary.items(), key=lambda item: item[1]))
    dictionary2 = dict(sorted(dictionary_excel.items(), key=lambda item: item[1][0]))
    print(f'Number of Items with itemTypeDisplayName: {item_number}')
    print(f'Number of Items without itemTypeDisplayName: {len(inventory_item_definition) - item_number}')
    # print(json.dumps(dictionary2, indent=2))
    write_to_json(dictionary1, "InventoryItemDefinitionFrequencies.json")
    write_to_excel(dictionary2, "InventoryItemDefinitionFrequencies.xlsx")

if __name__ == "__main__":
    pass
