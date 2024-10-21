import random
from irepela.homework_7.sorting import bubble_sort, gnome_sort, insert_sort, select_sort


rand_range = tuple(random.random() for _ in range(1000))


def test_sorting():
    for f in [bubble_sort, gnome_sort, insert_sort, select_sort]:
        for rev in [True, False]:
            assert (f(rand_range, reverse=rev) == sorted(rand_range, reverse=rev))
