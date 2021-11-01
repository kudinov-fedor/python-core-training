def remove_all_before(items: list, border: int) -> list:
    items_list = list()
    if border in items:
        index_el = items.index(border)
        items_list = items[index_el:]
    else:
        items_list = items
    return items_list
