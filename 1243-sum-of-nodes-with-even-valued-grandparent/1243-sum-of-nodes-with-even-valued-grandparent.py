# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(node, parent, grandparent):
            if not node:
                return 0
            left = dfs(node.left, node.val, parent)
            right = dfs(node.right, node.val, parent)
            curr = node.val if grandparent % 2 == 0 else 0
            return left + right + curr
        
        return dfs(root, -1, -1)