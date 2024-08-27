# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        min_move = 0

        def dfs(node):
            nonlocal min_move
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            min_move += abs(left) + abs(right)
        
            return node.val - 1 + left + right
        
        dfs(root)

        return min_move
