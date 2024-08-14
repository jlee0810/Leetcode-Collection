# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
            
        same_left = self.isSameTree(p.left, q.left)
        same_right = self.isSameTree(p.right, q.right)

        if same_left and same_right and p.val == q.val:
            return True
        else:
            return False