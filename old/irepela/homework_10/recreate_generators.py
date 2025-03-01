def my_zip(*iterable):
    """
    zip(*iterables) --> zip object

    Return a zip object whose .__next__() method returns a tuple where
    the i-th element comes from the i-th iterable argument.  The .__next__()
    method continues until the shortest iterable in the argument sequence
    is exhausted, and then it raises StopIteration.
    """
    iterators = [iter(i) for i in iterable]
    while True:
        try:
            yield tuple([next(i) for i in iterators])
        except StopIteration:
            return


def my_enumerate(iterable, start=0):
    """
    Return an enumerate object.

      iterable
        an object supporting iteration

    The enumerate object yields pairs containing a count (from start, which
    defaults to zero) and a value yielded by the iterable argument.

    enumerate is useful for obtaining an indexed list:
        (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
    """
    enumeration = range(start, len(iterable) + start)
    for item in zip(enumeration, iterable):
        yield item


def my_filter(key, iterable):
    """
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    """
    key = key or (lambda i: bool(i))
    for item in iterable:
        if key(item):
            yield item


def my_map(func, *iterables):
    """
    map(func, *iterables) --> map object

    Make an iterator that computes the function using arguments from
    each of the iterables.  Stops when the shortest iterable is exhausted.
    """
    for item in zip(*iterables):
        yield func(*item)
