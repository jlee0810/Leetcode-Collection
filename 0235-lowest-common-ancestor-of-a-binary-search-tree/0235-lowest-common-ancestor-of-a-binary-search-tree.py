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

            exists_left = dfs(node.left)
            exists_right = dfs(node.right)

            if exists_left and exists_right or node == p or node == q:
                return node
            else:
                return exists_left or exists_right
                
        return dfs(root)
            