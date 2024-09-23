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

            curr_path_max = max(left, right, 0) + node.val
            max_path = max(max_path, left + right + node.val, left + node.val, right + node.val, node.val)

            return curr_path_max
        
        dfs(root)

        return max_path