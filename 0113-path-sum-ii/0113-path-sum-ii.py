# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfs(node, combo):
            if not node:
                return
            
            combo.append(node.val)

            if sum(combo) == targetSum and not node.left and not node.right:
                result.append(combo.copy())
            else:
                if node.right: 
                    dfs(node.right, combo)
                if node.left:
                    dfs(node.left, combo)

            combo.pop()

        dfs(root, [])
        return result