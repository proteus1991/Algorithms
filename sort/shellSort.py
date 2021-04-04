"""
file: shellSort
about:
author: Xiaohong Liu
date: 20/04/20
"""
import random


def shellSort(alist):
    # time complexity is O(nlogn)< T < O(n^2)
    gap = len(alist) // 2

    while gap > 0:
        for start in range(gap):
            gapinsertionSort(alist, start, gap)
        gap = gap // 2


def gapinsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        currrentValue = alist[i]

        position = i

        while position > start and alist[position - gap] > currrentValue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currrentValue


if __name__ == "__main__":
    alist = [random.randint(1, 100) for _ in range(10)]
    print(alist)
    shellSort(alist)
    print(alist)