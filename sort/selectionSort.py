"""
file: selectionSort
about:
author: Xiaohong Liu
date: 20/04/20
"""

import random


def selectionSort(alist):
    # time complexity O(n^2)
    for i in range(len(alist) - 1, 0, -1):
        selected_index = 0
        for j in range(1, i + 1):
            if alist[j] > alist[selected_index]:
                selected_index = j

        alist[j], alist[selected_index] = alist[selected_index], alist[j]


if __name__ == "__main__":
    alist = [random.randint(1, 100) for _ in range(10)]
    print(alist)
    selectionSort(alist)
    print(alist)
