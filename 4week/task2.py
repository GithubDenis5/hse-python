"""
leetcode.com/problem-list/array/
https://leetcode.com/problems/maximum-subarray/description/?envType=problem-list-v2&envId=array&difficulty=MEDIUM
"""


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = current_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum
