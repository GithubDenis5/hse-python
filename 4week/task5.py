"""
leetcode.com/problem-list/array/
https://leetcode.com/problems/combination-sum/description/?envType=problem-list-v2&envId=array&difficulty=MEDIUM
"""


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        def backtrack(combination, start, target):
            if target == 0:
                result.append(list(combination))
                return
            elif target < 0:
                return

            for i in range(start, len(candidates)):
                combination.append(candidates[i])
                backtrack(combination, i, target - candidates[i])
                combination.pop()

        backtrack([], 0, target)
        return result
