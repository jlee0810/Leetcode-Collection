# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        result1, result2 = [], []

        def inorder(node, result):
            if node:
                inorder(node.left, result)
                result.append(node.val)
                inorder(node.right, result)
        inorder(root1, result1)
        inorder(root2, result2)

        merged_result = []
        i, j = 0, 0
        while i < len(result1) and j < len(result2):
            if result1[i] < result2[j]:
                merged_result.append(result1[i])
                i += 1
            else:
                merged_result.append(result2[j])
                j += 1

        while i < len(result1):
            merged_result.append(result1[i])
            i += 1

        while j < len(result2):
            merged_result.append(result2[j])
            j += 1

        return merged_result


                    