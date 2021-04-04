"""
file: binarySearch
about:
author: Xiaohong Liu
date: 20/04/20
"""

import random


def binarySearch(alist, item):
    # time complexity O(logn)
    if len(alist) < 1:
        return False
    mid = len(alist) // 2

    if alist[mid] == item:
        return True
    elif alist[mid] > item:
        return binarySearch(alist[:mid], item)
    else:
        return binarySearch(alist[mid+1:], item)


if __name__ == "__main__":
    alist = ([random.randint(1, 100) for _ in range(10)])
    alist.sort()
    item = alist[random.randrange(0, len(alist))]
    print(alist)
    print(item)
    print(binarySearch(alist, item))


