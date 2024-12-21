"""
leetcode.com/problem-list/binary-tree/
https://leetcode.com/problems/binary-tree-level-order-traversal/?envType=problem-list-v2&envId=binary-tree
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        curr = root
        while curr:
            if curr.left:
                r = curr.left
                while r.right:
                    r = r.right

                r.right = curr.right

                curr.right = curr.left
                curr.left = None

            curr = curr.right
