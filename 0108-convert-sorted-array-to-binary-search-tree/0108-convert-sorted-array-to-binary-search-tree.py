# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(left, right):
            if left > right:
                return 
            root_idx = (left + right) // 2
            root = TreeNode(nums[root_idx])
            root.left = dfs(left, root_idx - 1)
            root.right = dfs(root_idx + 1, right)
            return root

        return dfs(0, len(nums) - 1)