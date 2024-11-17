import io
import sys
import random
from tkupchyn.homework_07.sorting import select_sort, bubble_sort, gnome_sort, insert_sort


def test_time_it():
    rand_range = tuple(random.random() for _ in range(1000))
    buffer = io.StringIO()
    sys.stdout = buffer

    for f in [bubble_sort, gnome_sort, insert_sort, select_sort]:
        for rev in [True, False]:
            print(f(rand_range, reverse=rev) == sorted(rand_range, reverse=rev))

    sys.stdout = sys.__stdout__
    output = buffer.getvalue()
    buffer.close()

    assert 'nanoseconds' in output
