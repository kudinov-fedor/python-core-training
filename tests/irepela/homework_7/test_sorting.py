import random
from irepela.homework_7.sorting import bubble_sort, gnome_sort, insert_sort, select_sort


generate_range = lambda: tuple(random.random() for _ in range(1000))


def test_sorting():
    for f in [bubble_sort, gnome_sort, insert_sort, select_sort]:
        for rev in [True, False]:
            rand_range = generate_range()
            assert f(rand_range, reverse=rev) == sorted(rand_range, reverse=rev)
