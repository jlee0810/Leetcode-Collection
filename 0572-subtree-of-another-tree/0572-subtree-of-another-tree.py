# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False

            left_same = isSameTree(p.left, q.left)
            right_same = isSameTree(p.right, q.right)

            if left_same and right_same and p.val == q.val:
                return True
            else:
                return False

        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False

        left_sub = self.isSubtree(root.left, subRoot)
        right_sub = self.isSubtree(root.right, subRoot)

        if left_sub or right_sub or isSameTree(root, subRoot):
            return True
        else:
            return False
    