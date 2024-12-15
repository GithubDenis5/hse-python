"""
leetcode.com/problem-list/binary-tree/
https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/?envType=problem-list-v2&envId=binary-tree&difficulty=MEDIUM
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        def find_mid(start: ListNode, end: ListNode) -> ListNode:
            slow = fast = start
            while fast != end and fast.next != end:
                slow = slow.next
                fast = fast.next.next
            return slow

        def bst(start: ListNode, end: ListNode) -> Optional[TreeNode]:
            if start == end:
                return None

            mid = find_mid(start, end)
            root = TreeNode(mid.val)

            root.left = bst(start, mid)
            root.right = bst(mid.next, end)

            return root

        return bst(head, None)
