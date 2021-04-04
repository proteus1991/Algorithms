"""
file: mergeSort
about:
author: Xiaohong Liu
date: 20/04/20
"""

import random


def mergeSort(alist):
    # time complexity nlogn
    if len(alist) <= 1:
        return alist

    mid = len(alist) // 2

    leftList = mergeSort(alist[:mid])
    rightList = mergeSort(alist[mid:])

    mergedList = []
    while leftList and rightList:
        if leftList[0] < rightList[0]:              # 1, 2      # 3, 4
            mergedList.append(leftList.pop[0])
        else:
            mergedList.append(rightList.pop[0])

    mergedList.extend(leftList if leftList else rightList)

    return mergedList


if __name__ == "__main__":
    alist = [random.randint(1, 100) for _ in range(10)]
    print(alist)
    mergeSort(alist)
    print(alist)


