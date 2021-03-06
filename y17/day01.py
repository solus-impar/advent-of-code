"""Advent of Code 2017 Day 1: Inverse Captcha"""


def inverse_captcha(nums, match_around=False):
    """
    Args:
        nums (str): String of digits.

    Returns:
        sums (int): Sum of all digits that match the next digit in the string.

    Raises:
        None
    """

    sums = 0

    if match_around:
        diff = int(len(nums) / 2)
    else:
        diff = 1

    for i, j in enumerate(nums):
        if i + diff >= len(nums):
            ix = i + diff - len(nums)
        else:
            ix = i + diff

        if j == nums[ix]:
            sums += int(nums[ix])

    return sums
