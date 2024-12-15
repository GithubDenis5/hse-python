"""
leetcode.com/problem-list/binary-tree/
https://leetcode.com/problems/validate-binary-search-tree/description/?envType=problem-list-v2&envId=binary-tree&difficulty=MEDIUM
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node: TreeNode, l: float, u: float) -> bool:
            if not node:
                return True

            if not (l < node.val < u):
                return False

            return validate(node.left, l, node.val) and validate(
                node.right, node.val, u
            )

        return validate(root, float("-inf"), float("inf"))
