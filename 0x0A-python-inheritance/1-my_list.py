#!/usr/bin/python3
""" Module for my_list object """


class Heap:
    """ Heap data structure """
    def __init__(self, lst, size):
        self.lst = lst
        self.size = size

    @staticmethod
    def parent(i):
        """ Returns the parent of node i"""
        return i // 2

    @staticmethod
    def left(i):
        """ Returns the left of node i """
        return ((2 * i) + 1)

    @staticmethod
    def right(i):
        """ Returns the right of node i """
        return ((2 * i) + 2)

    def max_heapify(self, i):
        """ maintain the min heap property """
        while i < self.size:
            left = self.left(i)
            right = self.right(i)
            largest = i

            if left < self.size and self.lst[left] > self.lst[largest]:
                largest = left

            if right < self.size and self.lst[right] > self.lst[largest]:
                largest = right

            if largest == i:
                break
            temp = self.lst[i]
            self.lst[i] = self.lst[largest]
            self.lst[largest] = temp

            i = largest

    def build_max_heap(self):
        """ Builds min heap from unsorted array """
        n = self.size // 2 - 1

        while n >= 0:
            self.max_heapify(n)
            n -= 1

    def heap_sort(self):
        """ Sorts max heap in ascending order """
        n = self.size - 1
        for i in range(n, 0, -1):
            temp = self.lst[0]
            self.lst[0] = self.lst[i]
            self.lst[i] = temp
            self.size -= 1
            self.max_heapify(0)


class MyList(list):
    """ Object representation of MyList """
    def print_sorted(self):
        """ Sorts a list in ascending order """
        if not self or len(self) <= 0:
            pass
        else:
            new = self[:]
            heap = Heap(new, len(new))
            heap.build_max_heap()
            heap.heap_sort()
            print(new)
