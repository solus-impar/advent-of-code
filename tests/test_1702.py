"""Test Advent of Code 2017 Day 2"""
import numpy as np
from y17.day02 import corruption_checksum


def test_example():
    """Example from http://adventofcode.com/2017/day/2"""

    example = np.array([[5, 1, 9, 4],
                        [7, 5, 3, 3], # Repeated 3 in [7, 5, 3] to fill matrix
                        [2, 4, 6, 8]])

    assert corruption_checksum(example) == 18


def test_input():
    """Input from http://adventofcode.com/2017/day/2/input"""

    advent_input = np.loadtxt('data/1702.txt')

    assert corruption_checksum(advent_input) == 36174
