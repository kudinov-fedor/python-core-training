TEXT = "one one was a race horse, two two was one too."


def test_replace_required_arguments():
    """
    Two arguments are required.
    Old text as a first argument, new text as a second argument.
    """
    assert TEXT.replace("one", "three") == "three three was a race horse, two two was three too."


def test_replace_with_occurrences_number():
    """Can provide number of occurrences as a third argument.
    Default value is -1, which would remove all occurrences"""
    assert TEXT.replace("one", "three", -1) == "three three was a race horse, two two was three too."
    assert TEXT.replace("one", "three", 2) == "three three was a race horse, two two was one too."
