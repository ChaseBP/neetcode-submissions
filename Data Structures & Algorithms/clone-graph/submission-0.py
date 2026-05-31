"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        # Hashmap for storing old and new nodes
        oldToNew = {}

        def dfs(currNode):
            if currNode in oldToNew:
                return oldToNew[currNode]

            copy = Node(currNode.val)
            oldToNew[currNode] = copy

            for neighbor in currNode.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)