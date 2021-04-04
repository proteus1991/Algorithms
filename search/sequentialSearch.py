"""
file: sequentialSearch
about:
author: Xiaohong Liu
date: 20/04/20
"""
import random


def sequentialSearch(alist, item):
    # time complexity O(n)
    index = 0
    found = False

    while index < len(alist) and not found:
        if alist[index] == item:
            found = True
        else:
            index = index + 1

    return found


if __name__ == "__main__":
    alist = [random.randint(1, 100) for _ in range(10)]
    item = alist[random.randrange(0, len(alist))]
    print(alist)
    print(item)
    print(sequentialSearch(alist, item))