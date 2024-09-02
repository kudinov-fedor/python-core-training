# Create functions if your folder, and cover by tests as per assert examples provided here
# Implement functions body so that tests could pass.
# Implementing 'sorted' use 'min' and 'max' functions to implement sort logic.
# 

# Sort algorythm: 
# - Create empty list
# - take max / min value from input collection and put into new list
# - repeate same operation until input collection is empty.
# - return created list with sorted items 


def min(*args, key=None):
    return 0


def max(*args, key=None):
    return 0


def sorted(*args, key=None, reverse=False):
    """Ascending by default"""
    ...


if __name__ == "__main__":
    assert min(-7, -4, -2, 1, 2, 3, 4, 5, 6) == -7
    assert max(-7, -4, -2, 1, 2, 3, 4, 5, 6) == 6
    assert min(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs) == 1
    assert max(-7, -4, -2, 1, 2, 3, 4, 5, 6) == 6
    assert sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6) == [-7, -4, -2, 1, 2, 3, 4, 5, 6]
    assert sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6, reverse=True) == [6, 5, 4, 3, 2, 1, -2, -4, -7]
    assert sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs) == [1, -2, 2, 3, -4, 4, 5, 6, -7]
    assert sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs, reverse=True) == [-7, 6, 5, -4, 4, 3, -2, 2, 1]

    # can receive 1 positional parameter, which is a collection of items
    assert min([-7, -4, -2, 1, 2, 3, 4, 5, 6]) == -7
    assert max([-7, -4, -2, 1, 2, 3, 4, 5, 6]) == 6
    assert min([-7, -4, -2, 1, 2, 3, 4, 5, 6], key=abs) == 1
    assert max([-7, -4, -2, 1, 2, 3, 4, 5, 6]) == 6
    assert sorted([-7, -4, -2, 1, 2, 3, 4, 5, 6]) == [-7, -4, -2, 1, 2, 3, 4, 5, 6]
    assert sorted([-7, -4, -2, 1, 2, 3, 4, 5, 6], reverse=True) == [6, 5, 4, 3, 2, 1, -2, -4, -7]
    assert sorted([-7, -4, -2, 1, 2, 3, 4, 5, 6], key=abs) == [1, -2, 2, 3, -4, 4, 5, 6, -7]
    assert sorted([-7, -4, -2, 1, 2, 3, 4, 5, 6], key=abs, reverse=True) == [-7, 6, 5, -4, 4, 3, -2, 2, 1]
