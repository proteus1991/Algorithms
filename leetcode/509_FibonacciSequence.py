"""
file: 509_FibonacciSequence
about:
author: Xiaohong Liu
date: 30/04/20
"""

class Solution1:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        elif N == 1:
            return 1
        else:
            return self.fib(N-1) + self.fib(N-2)


class Solution:
    def __init__(self):
        self.fib_dict = {}

    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        elif N in self.fib_dict.keys():
            return self.fib_dict[N]
        else:
            result = self.fib(N-1) + self.fib(N-2)
            self.fib_dict[N] = result
            return result