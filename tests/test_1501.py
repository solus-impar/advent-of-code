"""Test Advent of Code 2015 Day 1"""
from y15.day01 import what_floor


def test_examples():
    """Examples from http://adventofcode.com/2015/day/1"""

    inputs = ['(())', '()()', '(((', '(()(()(', '))(((((', '())', '))(',
              ')))', ')())())']
    floors = [0, 0, 3, 3, 3, -1, -1, -3, -3]

    for i, j in zip(inputs, floors):
        assert what_floor(i) == j


def test_input():
    """Input from http://adventofcode.com/2015/day/1/input"""

    advent_file = open('data/1501.txt', 'r')
    advent_input = advent_file.read().strip()

    assert what_floor(advent_input) == 74
