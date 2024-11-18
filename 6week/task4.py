"""
leetcode.com/problem-list/sliding-window/
https://leetcode.com/problems/arithmetic-slices/submissions/1456063439/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM
"""


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        cn = 0
        cur = 0
        for i in range(2, n):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                cur += 1
                cn += cur
            else:
                cur = 0

        return cn
