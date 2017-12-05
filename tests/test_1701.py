"""Test Advent of Code 2017 Day 1"""
from y17.day01 import inverse_captcha


def examples():
    inputs = [1122, 1111, 1234, 91212129]
    sums = [3, 4, 0, 9]

    for i, j in zip(inputs, sums):
        assert inverse_captcha(i) == j
