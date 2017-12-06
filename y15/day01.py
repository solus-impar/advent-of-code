"""Advent of Code 2015 Day 1: Not Quite Lisp"""


def what_floor(directions):
    """
    Args:
        directions (str): String of parentheses.

    Returns:
        floor (int): Floor number.

    Raises:
        None
    """

    floor = 0

    for i in directions:
        if i == '(':
            floor += 1
        elif i == ')':
            floor -= 1

    return floor
