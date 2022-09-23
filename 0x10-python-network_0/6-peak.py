#!/usr/bin/python3

def peak(lst, low, high):
    """ Recursively find the peak
    """
    mid = (low + high) // 2
    if (low == mid or mid == high):
        return lst[mid]
    if (lst[mid] <= lst[mid - 1]):
        return peak(lst, low, mid)
    if (lst[mid] <= lst[mid + 1]):
        return peak(lst, mid, high)
    return lst[mid]


def find_peak(list_of_integers):
    """
    finds a peak in a given list of integers
    """
    if (list_of_integers):
        return peak(list_of_integers, 0, len(list_of_integers))
