"""
leetcode.com/problem-list/hash-table/
https://leetcode.com/problems/clone-graph/submissions/1429174776/?envType=problem-list-v2&envId=hash-table&difficulty=MEDIUM
"""


from typing import Optional, Dict


class Node:
    def __init__(self, val: int = 0, neighbors: Optional[list["Node"]] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        oldToNew: Dict[Node, Node] = {}

        def dfs(original_node: Node) -> Node:
            if original_node in oldToNew:
                return oldToNew[original_node]

            cloneNode = Node(original_node.val)
            oldToNew[original_node] = cloneNode

            for neighbor in original_node.neighbors:
                cloneNode.neighbors.append(dfs(neighbor))

            return cloneNode

        return dfs(node)
