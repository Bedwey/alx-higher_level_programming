#!/usr/bin/python3
"""
Find Peak task 6
"""


def find_peak(list_of_integers):
    """
    This function finds a peak in a list of unsorted integers.
    A peak is defined as an element that is greater
    than or equal to its neighbors.
    If there are multiple peaks, the function returns any one of them.
    """
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
