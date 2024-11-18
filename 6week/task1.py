"""
leetcode.com/problem-list/sliding-window/
https://leetcode.com/problems/longest-substring-without-repeating-characters/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM
"""


class Solution:
    def lOfLongestSubstring(self, s: str) -> int:
        c_index = {}
        max_l = 0
        start = 0

        for end, c in enumerate(s):
            if c in c_index and c_index[c] >= start:
                start = c_index[c] + 1
            c_index[c] = end
            max_l = max(max_l, end - start + 1)

        return max_l
