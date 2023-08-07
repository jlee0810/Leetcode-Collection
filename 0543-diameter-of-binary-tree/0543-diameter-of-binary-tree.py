# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiam = 0

        def diameterMeasure(node):
            if not node:
                return 0
            leftLength = diameterMeasure(node.left)
            rightLength = diameterMeasure(node.right)
            
            self.maxDiam = max(self.maxDiam, leftLength + rightLength)
            
            return max(leftLength, rightLength) + 1

        diameterMeasure(root)
        return self.maxDiam