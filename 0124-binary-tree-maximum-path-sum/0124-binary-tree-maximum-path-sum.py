# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = root.val
        def dfs(node):
            nonlocal max_path
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            curr = max(left, right, 0) + node.val
            max_path = max(max_path, left + node.val, right + node.val, left + right + node.val, node.val)

            return curr
        dfs(root)
        return max_path