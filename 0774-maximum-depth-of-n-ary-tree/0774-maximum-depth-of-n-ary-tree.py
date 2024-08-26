"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(node):
            if not node:
                return 0
            max_depth = 0
            for children in node.children:
                max_depth = max(dfs(children), max_depth)
            
            return max_depth + 1
        return dfs(root)

        