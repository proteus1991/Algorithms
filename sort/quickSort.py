"""
file: quickSort
about:
author: Xiaohong Liu
date: 20/04/20
"""

import random


def quickSort(alist, first, last):
    # time complexity O(nlogn), the worst case is O(n)
    if first >= last:
        return

    splitpoint = partition(alist, first, last, 'first')
    quickSort(alist, first, splitpoint - 1)
    quickSort(alist, splitpoint + 1, last)


def partition(alist, first, last, pivot_mode):
    if pivot_mode == 'first':
        pivot = alist[first]
    elif pivot_mode == 'last':
        alist[last], alist[first] = alist[first], alist[last]
        pivot = alist[first]
    else:
        rand_index = random.randrange(first, last)
        alist[rand_index], alist[first] = alist[first], alist[rand_index]
        pivot = alist[first]

    leftmark = first + 1
    rightmark = last

    while True:
        while leftmark <= rightmark and alist[leftmark] <= pivot:
            leftmark = leftmark + 1
        while leftmark <= rightmark and alist[rightmark] >= pivot:
            rightmark = rightmark - 1
        if leftmark <= rightmark:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
        else:
            break

    alist[first], alist[rightmark] = alist[rightmark], alist[first]

    return rightmark


if __name__ == "__main__":
    alist = [random.randint(1, 100) for _ in range(10)]
    print(alist)
    quickSort(alist, 0, len(alist)-1)
    print(alist)
