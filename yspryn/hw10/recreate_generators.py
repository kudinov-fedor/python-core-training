def my_zip(*iterable):

    position = 0
    min_length = min(len(item) for item in iterable)

    while position < min_length:
        res = []
        for i in range(len(iterable)):
            res.append(iterable[i][position])
        yield tuple(res)
        position += 1

    """
    zip(*iterables) --> zip object

    Return a zip object whose .__next__() method returns a tuple where
    the i-th element comes from the i-th iterable argument.  The .__next__()
    method continues until the shortest iterable in the argument sequence
    is exhausted and then it raises StopIteration.
    """


def my_enumerate(iterable, start=0):
    position = 0
    while position < len(iterable):
        yield start, iterable[position]
        start += 1
        position += 1

    """
    Return an enumerate object.

      iterable
        an object supporting iteration

    The enumerate object yields pairs containing a count (from start, which
    defaults to zero) and a value yielded by the iterable argument.

    enumerate is useful for obtaining an indexed list:
        (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
    """


# def my_filter(key, iterable):
    """
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    """


def my_map(func, *iterables):
    position = 0
    min_length = min(len(item) for item in iterables)

    while position < min_length:
        my_list = []
        for i in range(len(iterables)):
            my_list.append(iterables[i][position])
        yield func(*my_list)
        position += 1
    """
    map(func, *iterables) --> map object

    Make an iterator that computes the function using arguments from
    each of the iterables.  Stops when the shortest iterable is exhausted.
    """
