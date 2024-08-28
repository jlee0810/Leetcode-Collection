# Definition for a rope tree node.
# class RopeTreeNode(object):
#     def __init__(self, len=0, val="", left=None, right=None):
#         self.len = len
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getKthCharacter(self, root: Optional[object], k: int) -> str:
        """
        :type root: Optional[RopeTreeNode]
        """
        def dfs(node):
            if not node:
                return ""
            if not node.left and not node.right:
                return node.val
            left = dfs(node.left)
            right = dfs(node.right)

            return left + right
        
        word = dfs(root)
        return word[k - 1]