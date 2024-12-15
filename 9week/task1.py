"""
leetcode.com/problem-list/binary-tree/
https://leetcode.com/problems/unique-binary-search-trees/?envType=problem-list-v2&envId=binary-tree&difficulty=MEDIUM
"""


class Solution:
    def numTrees(self, n: int) -> int:
        a = [0] * (n + 1)
        a[0] = 1
        a[1] = 1

        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                l_t = a[root - 1]
                r_t = a[nodes - root]
                a[nodes] += l_t * r_t

        return a[n]
