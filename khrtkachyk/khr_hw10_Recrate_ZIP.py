def my_zip(*iterable):
    """
    zip(*iterables) --> zip object

    Return a zip object whose .__next__() method returns a tuple where
    the i-th element comes from the i-th iterable argument.  The .__next__()
    method continues until the shortest iterable in the argument sequence
    is exhausted, and then it raises StopIteration.
    """
    new_iterators = [iter(i) for i in iterable]

    while True:
        try:
            next_iterator = [next(j) for j in new_iterators]
            final_tuple = tuple(next_iterator)
            yield final_tuple
        except StopIteration:
            return


if __name__ == "__main__":

    a = ["a", "b", "c"]
    b = ["x", "y", "z"]
    print(list(my_zip(a, b)))

    assert list(zip(a, b)) == [("a", "x"), ("b", "y"), ("c", "z")]
    assert list(zip(a)) == [("a",), ("b",), ("c",)]
    assert list(my_zip(a, b)) == [("a", "x"), ("b", "y"), ("c", "z")]
    assert list(my_zip(a)) == [("a",), ("b",), ("c",)]
