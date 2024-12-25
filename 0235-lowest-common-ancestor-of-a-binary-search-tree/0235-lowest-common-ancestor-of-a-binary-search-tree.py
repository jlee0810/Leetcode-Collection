# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return
            left_contains = dfs(node.left)
            right_contains = dfs(node.right)

            if left_contains and right_contains or node == p or node == q:
                return node
            return left_contains or right_contains

        return dfs(root)