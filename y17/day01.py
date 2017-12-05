"""Day 1 - Advent of Code 2017"""


def inverse_captcha(nums):
    """Day 1: Inverse Captcha http://adventofcode.com/2017/day/1

    Args:
        nums (str): String of digits.

    Returns:
        sums (int): Sum of all digits that match the next digit in the string.

    Raises:
        None
    """

    sums = 0

    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            sums += int(nums[i])

    if nums[-1] == nums[0]:
        sums += int(nums[-1])

    return sums
