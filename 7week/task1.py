"""
leetcode.com/problem-list/sliding-window/
https://leetcode.com/problems/longest-repeating-character-replacement/submissions/1456067006/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_cn = {}
        max_freq = 0
        start = 0
        max_l = 0

        for end in range(len(s)):
            char = s[end]
            char_cn[char] = char_cn.get(char, 0) + 1
            max_freq = max(max_freq, char_cn[char])
            if (end - start + 1) - max_freq > k:
                char_cn[s[start]] -= 1
                start += 1
            max_l = max(max_l, end - start + 1)

        return max_l
