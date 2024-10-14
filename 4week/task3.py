"""
leetcode.com/problem-list/array/
https://leetcode.com/problems/jump-game/description/?envType=problem-list-v2&envId=array&difficulty=MEDIUM
"""


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        farthest = 0

        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])

        return True
