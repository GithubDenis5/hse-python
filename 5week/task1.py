"""
leetcode.com/problem-list/hash-table/
https://leetcode.com/problems/longest-substring-without-repeating-characters/?envType=problem-list-v2&envId=string&difficulty=MEDIUM
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        len_start = 0
        len_end = 0
        i = 0
        # current_max_string = ""
        while i < len(s):
            # new_str = current_max_string + s[i]
            pos = s.find(s[i], len_start, len_end)
            if pos == -1:
                len_end += 1
                i += 1
                if max_len < len_end - len_start:
                    max_len = len_end - len_start
            else:
                len_start = pos+1
                len_end += 1
                i += 1

        return max_len
