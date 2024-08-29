# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        count = 0

        def dfs(node):
            nonlocal count
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            left = dfs(node.left)
            right = dfs(node.right)

            for dist_left in left:
                for dist_right in right:
                    if dist_left + dist_right <= distance:
                        count += 1
            leaves = left + right
            for i in range(len(leaves)):
                leaves[i] += 1
            
            return leaves

        dfs(root)
        return count