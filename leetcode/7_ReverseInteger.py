"""
file: 7_ReverseInteger
about:
author: Xiaohong Liu
date: 20/04/20
"""


class Solution:
    def reverse(self, x: int) -> int:
        if x < -2 ** 31 or x > 2 ** 31 - 1:
            return 0
        x = [i for i in str(x)]
        if x[0] == '-':
            x = ['-'] + [x.pop() for _ in range(len(x)-1)]
        else:
            x = [x.pop() for _ in range(len(x))]
        x = int(''.join(x))
        return 0 if x < -2 ** 31 or x > 2 ** 31 - 1 else x

