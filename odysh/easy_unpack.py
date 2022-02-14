"""
Create a function that gets a tuple and returns a tuple with 3 elements - the first,
third and second element from the last for the given array.
"""

def easy_unpack(elements: tuple) -> tuple:
    """
        returns a tuple with 3 elements - first, third and second to the last
    """
    return (elements[0], elements[2], elements[-2])