def chain_sum(number=0):
    """
      Function which returns itself if arguments are passed,
      and returns numbers sum if no arguments are passed

      Args:
          number: int number

      Returns:
          itself or numbers sum
    """
    result = number

    def inner_sum(local_number=0):
        nonlocal result

        if local_number:
            result += local_number
            return inner_sum

        return result

    return inner_sum
