def unpack_while_loop(items: list) -> list:
    """
      Flattens list using while

      Args:
          items: nested list of items

      Returns:
          list: flattened list
    """
    unpacked = []
    copied_list = list(reversed(items))
    while len(copied_list) > 0:
        next_item = copied_list.pop()
        if isinstance(next_item, list):
            copied_list.extend(reversed(next_item))
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
