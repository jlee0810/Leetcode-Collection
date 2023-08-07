# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balance(node):
            if not node:
                return 0
            leftBalanced = balance(node.left)
            rightBalanced = balance(node.right)

            if leftBalanced == - 1 or rightBalanced == -1 or abs(leftBalanced - rightBalanced) > 1:
                return -1
            return max(leftBalanced, rightBalanced) + 1

        if balance(root) != -1:
            return True 
        return False