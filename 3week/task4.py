"""
leetcode.com/problem-list/array/
https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/1412790080/?envType=problem-list-v2&envId=array&difficulty=MEDIUM
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i

        return -1
