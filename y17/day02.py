"""Advent of Code 2017 Day 2: Corruption Checksum"""


def corruption_checksum(A):
    """
    Args:
        A (numpy.matrix): The spreadsheet as a NumPy matrix.

    Returns:
        checksum (int): Sum of each row's difference in max and min.

    Raises:
        None
    """

    checksum = 0

    for row in A:
        checksum += int(row.max() - row.min())

    return checksum
