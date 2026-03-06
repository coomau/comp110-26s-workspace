"""EX04 - List Utility Functions - implement algorithms to practice computational thinking."""

__author__: str = "730736150"


def all(input: list[int], value: int) -> bool:
    """True if whole list of input is equal to value."""
    if len(input) == 0:
        return False
    for item in input:
        if item != value:
            return False
    return True


def max(input: list[int]) -> int:
    """Return the largest number in input"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    largest: int = input[0]
    for item in input:
        if item > largest:
            largest = item  # i felt pretty smart figuring this one out, since its going through the whole list, if the next indicacy is larger than the current largest, it becomes the largest and so on
    return largest


def is_equal(
    a: list[int], b: list[int]
) -> (
    bool
):  # i had these values as x and y until i got to part 4, where it was labeled a and b, so i just changed them to a and b.
    """Return True if lists a and b are equal."""
    if len(a) != len(b):
        return False
    i: int = (
        0  # just using this as a placeholder cause it was easier to increment in a seperate value.
    )
    while i < len(a):
        if a[i] != b[i]:
            return False
        i = (
            i + 1
        )  # i don't really know if this is necessary, but it's essentially going through the list for every integer and checking the integer at the same position in the other list. if they don't match it returns false, if they do it proceeds to the next value and so on.
    return True


def extend(a: list[int], b: list[int]) -> None:
    """Mutate list a by appending all elements of list b to the end."""
    for item in b:
        a.append(item)
