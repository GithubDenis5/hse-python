"""
leetcode.com/problem-list/string/
https://leetcode.com/problems/zigzag-conversion/?envType=problem-list-v2&envId=string&difficulty=MEDIUM
"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        list_ind = []

        result = ""

        curr_ind = 0
        flag = 1  # True = up
        if numRows == 1:
            return s
        for c in s:
            if flag == 1 and curr_ind != numRows:
                curr_ind += 1
            elif flag == 2 and curr_ind != 1:
                curr_ind -= 1
            elif curr_ind == numRows:
                flag = 2
                curr_ind -= 1
            elif curr_ind == 1:
                flag = 1
                curr_ind += 1
            list_ind.append([c, curr_ind])

        for i in range(numRows):
            for pair in list_ind:
                if pair[1] == i+1:
                    result += pair[0]

        return result
