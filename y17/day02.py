"""Advent of Code 2017 Day 2: Corruption Checksum"""


def corruption_checksum(sheet, divide=False):
    """
    Args:
        sheet (numpy.matrix): The spreadsheet as a NumPy matrix.

    Returns:
        checksum (int): Sum of each row's difference in max and min.

    Raises:
        None
    """

    checksum = 0

    for row in sheet:
        if divide:
            for i in row:
                for j in row:
                    if i != j and i % j == 0:
                        checksum += int(i / j)

        else:
            checksum += int(row.max() - row.min())

    return checksum
