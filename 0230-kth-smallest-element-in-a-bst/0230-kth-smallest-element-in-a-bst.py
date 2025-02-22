# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            nonlocal k
            if not node:
                return node
            left = inorder(node.left)
            if left is not None:
                return left
            k -= 1
            if k == 0:
                return node.val
            right = inorder(node.right)
            return right
        
        return inorder(root)