"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def getDepth(self, node):
        depth = 0
        while node:
            node = node.parent
            depth += 1
        return depth

    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        #First attempt not memory efficient
        # root = p
        # while root.parent:
        #     root = root.parent

        # def dfs(node):
        #     if not node or node == p or node == q:
        #         return node
        #     left, right = dfs(node.left), dfs(node.right)
        #     return node if left and right else left or right
        
        # return dfs(root)

        #Second Attempt
        pDepth = self.getDepth(p)
        qDepth = self.getDepth(q)

        for _ in range(pDepth - qDepth):
            p = p.parent
        for _ in range(qDepth - pDepth):
            q = q.parent
        while p != q:
            p = p.parent
            q = q.parent
        return q