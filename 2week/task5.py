"""
leetcode.com/problem-list/string/
https://leetcode.com/problems/longest-palindromic-substring/submissions/1406850608/?envType=problem-list-v2&envId=string&difficulty=MEDIUM
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:

        start = 0
        end = 0

        def expCent(s, left_idx, right_idx):
            while left_idx >= 0 and right_idx < len(s) and s[left_idx] == s[right_idx]:
                left_idx -= 1
                right_idx += 1

            return right_idx - left_idx - 1

        for idx in range(len(s)):
            len_odd = expCent(s, idx, idx)
            len_even = expCent(s, idx, idx + 1)
            max_len = max(len_odd, len_even)

            if max_len > end - start:
                start = idx - (max_len - 1) // 2
                end = idx + max_len // 2

        return s[start:end + 1]
