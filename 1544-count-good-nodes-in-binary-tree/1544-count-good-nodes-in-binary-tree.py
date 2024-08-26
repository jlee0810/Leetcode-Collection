# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(node, max_val):
            nonlocal count
            if not node:
                return
            if node.val >= max_val:
                count += 1
            dfs(node.left, max(max_val, node.val))
            dfs(node.right, max(max_val, node.val))
        
        dfs(root, root.val)
        return count

        # count = 0
        # q = deque()
        # q.append((root, root.val))
        
        # while q:
        #     curr_node, curr_max = q.popleft()
        #     if curr_node.val >= curr_max:
        #         count += 1
        #     if curr_node.left:
        #         q.append((curr_node.left, max(curr_max, curr_node.val)))
        #     if curr_node.right:
        #         q.append((curr_node.right, max(curr_max, curr_node.val)))
            
        # return count