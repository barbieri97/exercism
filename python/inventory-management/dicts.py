""" funções para manejo de inventário """


from collections import Counter

def create_inventory(items: list) -> dict:
    """

    :param items: list - list of items to create an inventory from.
    :return:  dict - the inventory dictionary.
    """

    return {k: items.count(k) for k in items}


def add_items(inventory: dict, items: list) -> dict:
    """

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return:  dict - the inventory dictionary update with the new items.
    """

    new_inventory = create_inventory(items)
    return dict(Counter(inventory) + Counter(new_inventory))


def decrement_items(inventory: dict, items: list) -> dict:
    """

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return:  dict - updated inventory dictionary with items decremented.
    """

    for item in items:
        if inventory[item] > 0:
            inventory[item] -= 1
    return inventory

def remove_item(inventory: dict, item: list) -> dict:
    """
    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return:  dict - updated inventory dictionary with item removed.
    """

    if item in inventory:
        del inventory[item]
    return inventory

def list_inventory(inventory: dict) -> list:
    """

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    return [(k, v) for k, v in zip(inventory.keys(), inventory.values()) if v > 0]
