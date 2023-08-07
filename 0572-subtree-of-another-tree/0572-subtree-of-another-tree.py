# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        leftSame = self.isSameTree(p.left, q.left)
        rightSame = self.isSameTree(p.right, q.right)

        if p.val == q.val and leftSame and rightSame:
            return True
        return False
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return False
            currentSame = self.isSameTree(root, subRoot)
            leftSame = dfs(root.left)
            rightSame = dfs(root.right)
            
            return currentSame or leftSame or rightSame
            
        return dfs(root)