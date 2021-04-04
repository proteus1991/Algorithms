"""
file: 3_Longest Substring Without Repeating Characters
about:
author: Xiaohong Liu
date: 20/04/20
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        smax = 0

        for i in range(len(s)):
            sset = set()
            j = i
            temp_max = 0
            while j < len(s):
                if s[j] not in sset:
                    sset.add(s[j])
                    temp_max = temp_max + 1
                else:
                    break
                j = j + 1
                if temp_max > smax:
                    smax = temp_max
        return smax