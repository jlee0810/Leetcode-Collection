# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        flatten_tree = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            flatten_tree.append(node)
            inorder(node.right)
        
        inorder(root)
        for idx, node in enumerate(flatten_tree):
            if node == p:
                return flatten_tree[idx + 1] if idx + 1 < len(flatten_tree) else None