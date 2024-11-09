from itertools import chain


def unpack_while_loop(arguments):
    """
    Function converts the arguments
    into a list and  as a result,  it creates a new list from popped elements
    """

    arg_list = list(arguments)
    result = list()

    while arg_list:
        element = arg_list.pop()
        if isinstance(element, (list, tuple)):
            arg_list.extend(element)
        elif isinstance(element, dict):
            arg_list.extend(chain.from_iterable(element.items()))
        else:
            result.append(element)

    return result[::-1]


def unpack_recursive(arguments):
    """
    Function adds the new argument to the list if it is not a list, tuple, or dict.
    If the argument is a list, tuple or dict, the function is called recursively.
    """

    result = list()

    for arg in arguments:
        if isinstance(arg, (list, tuple)):
            result.extend(unpack_recursive(arg))
        elif isinstance(arg, dict):
            result.extend(unpack_recursive(arg.items()))
        else:
            result.append(arg)

    return result


def unpack_while_loop_gen(arguments):
    """
    Generator creates the new object from popped elements
    """

    arg_list = list(arguments)

    assert arg_list

    while arg_list:
        element = arg_list.pop(0)

        if isinstance(element, list):
            arg_list = element + arg_list
        elif isinstance(element, tuple):
            arg_list = list(element) + arg_list
        elif isinstance(element, dict):
            arg_list = list(element.items()) + arg_list
        else:
            yield element


def unpack_recursive_gen(arguments):
    """
   Generator yields the argument if it is not a list, or tuple.
    If the argument is a list, or tuple the function is called recursively.
    """

    for arg in arguments:
        if isinstance(arg, (list, tuple)):
            yield from unpack_recursive(arg)
        elif isinstance(arg, dict):
            yield from unpack_recursive(arg.items())
        else:
            yield arg


if __name__ == "__main__":
    arguments = [123, ["234", None], {"sdf": True, "bb": 44}, {(1, 2, 3): "abc"}]
    print(unpack_while_loop(arguments))
    print(unpack_recursive(arguments))
    print(list(unpack_while_loop_gen(arguments)))
    print(list(unpack_recursive_gen(arguments)))
