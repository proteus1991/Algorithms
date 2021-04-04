"""
file: bubbleSort
about:
author: Xiaohong Liu
date: 20/04/20
"""
import random


def bubbleSort(alist):
    # time complexity O(n^2)
    for i in range(len(alist)-1, 0, -1):
        for j in range(i):
            if alist[j+1] < alist[j]:
                alist[j+1], alist[j] = alist[j], alist[j+1]


if __name__ == "__main__":
    alist = [random.randint(1, 100) for _ in range(10)]
    print(alist)
    bubbleSort(alist)
    print(alist)
