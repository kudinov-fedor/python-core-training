def to_int(binary_str: str) -> int:
    """
    Converts binary string to decimal number and returns result.

    Usage Example:
           convert_binary_to_decimal('1010101') == 181

     Args:
         binary_str (str): Binary string.

     Returns:
         int: Decimal number.
     """
    return int(binary_str, 2)


def convert_to_list(dict_to_convert: dict) -> list:
    """
     Converts dictionary to a list and returns result.

    Args:
        dict_to_convert (str): Dictionary to convert.

    Returns:
        list: of dictionary or set.
    """
    return sorted(list(dict_to_convert))


def as_tuple(dict_to_convert: dict) -> tuple:
    """
      Converts dictionary to a tuple and returns result.

     Args:
         dict_to_convert (str): Dictionary to convert.

     Returns:
         tuple: of dictionary or set.
     """
    return tuple(sorted(dict_to_convert))


def convert_to_set(collection_to_convert) -> set:
    """
       Converts input collection to a set and returns result.

      Args:
          collection_to_convert: Input collection to convert.

      Returns:
          set: of converted collection
      """
    return set(sorted(collection_to_convert))
