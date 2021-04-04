"""
file: 204_CountPrimes
about:
author: Xiaohong Liu
date: 30/04/20
"""
import math


class Solution1:
    def countPrimes(self, n: int) -> int:
        n = n-1
        if 0 < n <= 3:
            return n-1
        elif n == 0:
            return 0
        elif n % 2 ==0:
            return 0
        else:
            return self.isPrimes(n) + self.countPrimes(n - 1)

    def isPrimes(self, n):
        i = n - 1
        while i > 1:
            if n % i == 0:
                return 0
            i = i-1
        return 1


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        alist = [0, 0, 1] + [1, 0] * ((n-2) //2)
        for i in range(3, math.ceil((math.sqrt(n)))):
            if alist[i] == 1:
                for j in range(i*i, n, i):
                    alist[j] = 0
        return sum(alist)


if __name__ == '__main__':
    S = Solution1()
    print(S.countPrimes(10))