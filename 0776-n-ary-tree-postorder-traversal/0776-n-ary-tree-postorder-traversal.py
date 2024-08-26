"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        def post(node):
            if not node:
                return node
            for children in node.children:
                post(children)
            result.append(node.val)
        post(root)
        return result