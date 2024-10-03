def check_default_bool() -> bool:
    """
      Check if bool by default is True or false

      Returns:
          bool: result of default bool object
      """
    return bool()


def check_bool_instance(type_to_check) -> bool:
    """
      Check if some type is bool instance

      Returns:
          bool: result of conversion bool to type
      """
    some_bool = bool()
    return isinstance(some_bool, type_to_check)
