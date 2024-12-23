"""
leetcode.com/problem-list/array/
https://leetcode.com/problems/jump-game/description/?envType=problem-list-v2&envId=array&difficulty=MEDIUM
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            max_area = max(max_area, min(height[left], height[right]) * width)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
