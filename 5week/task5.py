"""
leetcode.com/problem-list/hash-table/
https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=problem-list-v2&envId=hash-table&difficulty=MEDIUM
"""


from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numSet = set(nums)
        longestSeq = 0

        for num in numSet:

            if num - 1 not in numSet:
                currNum = num
                currStreak = 1

                while currNum + 1 in numSet:
                    currNum += 1
                    currStreak += 1

                longestSeq = max(longestSeq, currStreak)

        return longestSeq
