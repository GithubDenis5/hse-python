"""
leetcode.com/problem-list/sliding-window/
https://leetcode.com/problems/fruit-into-baskets/submissions/1462148584/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM
"""

from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        b = defaultdict(int)
        start = 0
        max_f = 0

        for end in range(len(fruits)):
            b[fruits[end]] += 1

            while len(b) > 2:
                b[fruits[start]] -= 1
                if b[fruits[start]] == 0:
                    del b[fruits[start]]
                start += 1

            max_f = max(max_f, end - start + 1)

        return max_f
