# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append((root, float('-inf'), float('inf')))

        while q:
            curr_node, min_val, max_val = q.popleft()
            
            if curr_node.val <= min_val or curr_node.val >= max_val:
                return False
            
            if curr_node.left:
                q.append((curr_node.left, min_val, curr_node.val))
            
            if curr_node.right:
                q.append((curr_node.right, curr_node.val, max_val))
        
        return True


        # def dfs(node, min_val, max_val):
        #     if not node:
        #         return True
        #     if min_val >= node.val or max_val <= node.val:
        #         return False
        #     left = dfs(node.left, min_val, node.val)
        #     right = dfs(node.right, node.val, max_val)
        #     if left and right:
        #         return True
        #     else:
        #         return False
        # return dfs(root, float(-inf), float(inf))            