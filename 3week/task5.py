"""
leetcode.com/problem-list/array/
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/?envType=problem-list-v2&envId=array&difficulty=MEDIUM
"""


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        leftIndex = left

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        rightIndex = right

        if leftIndex <= rightIndex and rightIndex < len(nums) and nums[leftIndex] == target and nums[rightIndex] == target:
            return [leftIndex, rightIndex]
        return [-1, -1]
