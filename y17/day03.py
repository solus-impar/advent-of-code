"""Advent of Code 2017 Day 3: Spiral Memory"""
import numpy as np


def spiral_memory(square):
    """
    Args:
        square (int): Square in the spiral memory.

    Returns:
        steps (int): Number of steps away `square` is from `1`.

    Raises:
        None
    """

    steps = 1
    while steps ** 2 <= square:
        steps += 2

    corners = np.zeros(4)
    for i in range(4):
        corners[i] = (steps ** 2) - (i * (steps - 1))

    steps -= 1 + int(np.absolute(corners - square).min())

    return steps
