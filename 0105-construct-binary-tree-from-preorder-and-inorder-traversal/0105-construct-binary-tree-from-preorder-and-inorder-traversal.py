# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder:
            return
        
        root = TreeNode(preorder[0])
        inorder_root = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1: inorder_root + 1], inorder[: inorder_root])
        root.right = self.buildTree(preorder[inorder_root + 1 : ], inorder[inorder_root + 1: ])
        
        return root

        