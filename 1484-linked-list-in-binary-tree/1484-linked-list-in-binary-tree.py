# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(t_node, l_node):
            if not l_node:
                return True
            if not t_node:
                return False
            if t_node.val != l_node.val:
                return False
            return dfs(t_node.left, l_node.next) or dfs(t_node.right, l_node.next)
        
        def traverse_tree(tree_node):
            if not tree_node:
                return False
            return dfs(tree_node, head) or traverse_tree(tree_node.left) or traverse_tree(tree_node.right)

        return traverse_tree(root)