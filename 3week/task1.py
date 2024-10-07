"""
leetcode.com/problem-list/array/
https://leetcode.com/problems/largest-number/?envType=problem-list-v2&envId=array&status=SOLVED
"""


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        string_nums = list(map(str, nums))

        for i in range(len(string_nums)):
            for j in range(len(string_nums) - 1 - i):
                if not (string_nums[j] + string_nums[j + 1] > string_nums[j + 1] + string_nums[j]):
                    string_nums[j], string_nums[j + 1] = string_nums[j + 1], string_nums[j]

        res = ''.join(string_nums)

        if res[0] == '0':
            return '0'
        else:
            return res
