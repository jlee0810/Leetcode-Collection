# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        left_balanced = self.isBalanced(root.left)
        right_balanced = self.isBalanced(root.right)

        if left_balanced and right_balanced and abs(left_balanced - right_balanced) <= 1:
            return max(left_balanced, right_balanced) + 1
        else:
            return False