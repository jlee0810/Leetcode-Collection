# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def balanced(node):
            if not node:
                return True
            
            left_balanced = balanced(node.left)
            right_balanced = balanced(node.right)
    
            if left_balanced and right_balanced and abs(left_balanced - right_balanced) <= 1:
                return max(left_balanced, right_balanced) + 1
            else:
                return False
        result = balanced(root)
        if not result:
            return False
        else:
            return True