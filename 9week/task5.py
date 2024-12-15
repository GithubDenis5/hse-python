"""
leetcode.com/problem-list/binary-tree/
https://leetcode.com/problems/recover-binary-search-tree/submissions/1479499600/?envType=problem-list-v2&envId=binary-tree&difficulty=MEDIUM
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        first = None
        second = None
        prev = None

        def recover(node: TreeNode):
            nonlocal first, second, prev
            if not node:
                return

            recover(node.left)

            if prev and node.val < prev.val:
                if not first:
                    first = prev
                second = node

            prev = node

            recover(node.right)

        recover(root)

        if first and second:
            first.val, second.val = second.val, first.val
