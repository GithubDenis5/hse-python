"""
leetcode.com/problem-list/string/
https://leetcode.com/problems/generate-parentheses/submissions/1402735736/?envType=problem-list-v2&envId=string
"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        comb_list = []

        def genvar(curr_str, open_cn, close_cn):
            if len(curr_str) == 2 * n:
                comb_list.append(curr_str)
                return

            if open_cn < n:
                genvar(curr_str + '(', open_cn + 1, close_cn)

            if close_cn < open_cn:
                genvar(curr_str + ')', open_cn, close_cn + 1)

        genvar("", 0, 0)

        print(comb_list)
        return comb_list
