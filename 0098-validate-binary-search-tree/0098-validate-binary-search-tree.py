# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, min, max):
            if not node:
                return True
            if node.val <= min or node.val >= max:
                return False
            if not dfs(node.left, min, node.val):
                return False
            if not dfs(node.right, node.val, max):
                return False
            return True
            
        return dfs(root, float('-inf'), float('inf'))