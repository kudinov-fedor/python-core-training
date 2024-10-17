def unpack_while_loop(items: list) -> list:
    """
      Flattens list with up to 3 levels of nesting

      Args:
          items: list of items with up to 3 levels of nesting

      Returns:
          list: flattened list
    """
    unpacked = []
    copied_list = list(reversed(items))
    while len(copied_list) > 0:
        next_item = copied_list.pop()
        if isinstance(next_item, list):
            nested_list_1 = list(reversed(next_item))
            while len(nested_list_1) > 0:
                next_item = nested_list_1.pop()
                if isinstance(next_item, list):
                    nested_list_2 = list(reversed(next_item))
                    while len(nested_list_2) > 0:
                        next_item = nested_list_2.pop()
                        if isinstance(next_item, list):
                            unpacked.extend(next_item)
                        else:
                            unpacked.append(next_item)
                else:
                    unpacked.append(next_item)
        else:
            unpacked.append(next_item)
    return unpacked


def unpack_recursive(items: list) -> list:
    """
      Flattens list using recursion

      Args:
          items: list of items with unlimited level of nesting

      Returns:
          list: flattened list
    """
    unpacked = []
    for item in items:
        if isinstance(item, list):
            unpacked.extend(unpack_recursive(item))
        else:
            unpacked.append(item)
    return unpacked
