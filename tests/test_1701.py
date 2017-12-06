"""Test Advent of Code 2017 Day 1"""
from y17.day01 import inverse_captcha


def test_examples():
    """Examples from http://adventofcode.com/2017/day/1"""

    part1_inputs = ['1122', '1111', '1234', '91212129']
    part1_sums = [3, 4, 0, 9]

    part2_inputs = ['1212', '1221', '123425', '123123', '12131415']
    part2_sums = [6, 0, 4, 12, 4]

    for i, j in zip(part1_inputs, part1_sums):
        assert inverse_captcha(i, False) == j

    for i, j in zip(part2_inputs, part2_sums):
        assert inverse_captcha(i, True) == j


def test_input():
    """Input from http://adventofcode.com/2017/day/1/input"""

    advent_file = open('data/1701.txt', 'r')
    advent_input = advent_file.read().strip()

    assert inverse_captcha(advent_input, False) == 1034
    assert inverse_captcha(advent_input, True) == 1356
