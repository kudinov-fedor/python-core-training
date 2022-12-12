from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    if len(elements) < 2:
        return True
    first_element = elements[0]
    return all(element == first_element for element in elements)


def all_the_same_set(elements: List[Any]) -> bool:
    return len(set(elements)) <= 1


print(all_the_same_set([1, 2, 1]))
