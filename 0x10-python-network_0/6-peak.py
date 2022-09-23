#!/usr/bin/python3
"""
Module for peak finding
"""


def peak(lst, low, high):
    """ Recursively find the peak
    """
    mid = (low + high - 1) // 2
    if (mid - 1 < 0 or mid + 1 >= high):
        return lst[mid]
    if (lst[mid - 1] < lst[mid] and lst[mid + 1] < lst[mid]):
        return lst[mid]
    if (lst[mid] < lst[mid + 1]):
        return peak(lst, mid + 1, high)
    return peak(lst, low, mid)


def find_peak(list_of_integers):
    """
    finds a peak in a given list of integers
    """
    if (list_of_integers):
        return peak(list_of_integers, 0, len(list_of_integers))
