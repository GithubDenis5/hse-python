"""
leetcode.com/problem-list/sliding-window/
https://leetcode.com/problems/permutation-in-string/description/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM
"""

from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 > len_s2:
            return False

        s1_cn = Counter(s1)
        wnd_cn = Counter(s2[:len_s1])

        if s1_cn == wnd_cn:
            return True

        for i in range(len_s1, len_s2):
            start_c = s2[i - len_s1]
            end_c = s2[i]
            wnd_cn[start_c] -= 1
            if wnd_cn[start_c] == 0:
                del wnd_cn[start_c]

            wnd_cn[end_c] += 1

            if wnd_cn == s1_cn:
                return True

        return False
