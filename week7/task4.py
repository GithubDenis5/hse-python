"""
leetcode.com/problem-list/sliding-window/
https://leetcode.com/problems/subarray-product-less-than-k/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM
"""


class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0

        p = 1
        cn = 0
        start = 0

        for end in range(len(nums)):
            p *= nums[end]
            while p >= k:
                p //= nums[start]
                start += 1

            cn += end - start + 1

        return cn
