"""Test Advent of Code 2017 Day 3"""
from y17.day03 import spiral_memory


def test_examples():
    """Examples from http://adventofcode.com/2017/day/3"""

    examples = [1, 12, 23, 1024]
    steps = [0, 3, 2, 31]

    for i, j in zip(examples, steps):
        assert spiral_memory(i) == j

    assert spiral_memory(347991) == 480 # puzzle input
