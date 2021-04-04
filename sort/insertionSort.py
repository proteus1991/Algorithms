"""
file: insertionSort
about:
author: Xiaohong Liu
date: 20/04/20
"""
import random


def insertionSort(alist):
    # time complexity O(n^2)
    for i in range(1, len(alist)):
        currrentValue = alist[i]

        position = i

        while position > 0 and alist[position - 1] > currrentValue:
            alist[position] = alist[position - 1]
            position = position - 1

        alist[position] = currrentValue


if __name__ == "__main__":
    alist = [random.randint(1, 100) for _ in range(10)]
    print(alist)
    insertionSort(alist)
    print(alist)
