import random


# def quick_sort(alist, first, last):
#     if first >= last:
#         return
#     mid_value = alist[first]
#     low = first + 1
#     high = last
#     while True:
#         while low <= high and alist[low] <= mid_value:
#             low += 1
#         while low <= high and alist[high] >= mid_value:
#             high -= 1
#         if low <= high:
#             alist[low], alist[high] = alist[high], alist[low]
#         else:
#             break
#
#     alist[first], alist[high] = alist[high], alist[first]
#
#     quick_sort(alist, first, high-1)
#     quick_sort(alist, high+1, last)


def quick_sort(alist, first, last):
    if first >= last:
        return
    mid_value = alist[first]
    low = first
    high = last
    while low < high:
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]

    alist[low] = mid_value

    quick_sort(alist, first, low-1)
    quick_sort(alist, low+1, last)


if __name__ == "__main__":
    alist = [random.randint(1, 100) for _ in range(10)]
    print(alist)
    quick_sort(alist, 0, len(alist)-1)
    print(alist)