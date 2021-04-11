# First interview

# Given a positive integer n,
# find the least number of perfect square numbers
# and corresponding combination of perfect square number
# (for example, 1, 4, 9, 16, ...) which sum to n.

# EXAMPLE1:
# Input: n = 13
# Output: [2, [4, 9]]
# Explanation: 13 = 4 + 9.
# EXAMPLE2:
# Input: n = 12
# Output: [3, [4, 4, 4]]
# Explanation: 12 = 4 + 4 + 4.
from math import ceil, sqrt


def getMinSquares(n):
    # base cases
    if n <= 3:
        return n

    # getMinSquares rest of the table
    # using recursive formula
    res = n  # Maximum squares required
    # is n (1 * 1 + 1 * 1 + ..)

    # Go through all smaller numbers
    # to recursively find minimum
    for x in range(1, n + 1):
        temp = x * x
        if temp > n:
            break
        else:
            res = min(res, 1 + getMinSquares(n - temp))

    return res


def leastPerfectSquare(n):
    if n <= 3:
        return [n, [1] * n]
    num = n
    for i in range(1, n + 1):
        square = i * i

        if square > n:
            break
        else:
            if num >= 1 + leastPerfectSquare(n - square)[0]:
                alist = [i * i] + leastPerfectSquare(n - square)[1]
            num = min(num, 1 + leastPerfectSquare(n - square)[0])
    return [num, alist]


def dpleastPerfectSquare(n):
    dp = [0, 1, 2, 3]
    alist = [0]*(n+1)
    max_square = 0
    for i in range(4, n + 1):
        dp += [i]
        for x in range(1, ceil(sqrt(i)) + 1):
            square = x * x

            if square > n:
                break
            else:
                if dp[i] > 1 +dp[i-square]:
                    dp[i] = 1 + dp[i - square]
                    max_square = square
            alist[i] = max_square
    blist = []
    while n > 0:
        blist.append(alist[n])
        n = n - alist[n]

    return [dp[-1], blist]



if __name__ == '__main__':
    n = 5
    print(getMinSquares(n))
    # print(dpleastPerfectSquare(n))
