# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        in_node = defaultdict(int)
        child_list = defaultdict(list)

        for description in descriptions:
            parent, child, isLeft = description
            in_node[child] += 1
            child_list[parent].append((child, isLeft))
        
        root = TreeNode()

        for description in descriptions:
            num, _, _ = description
            if num not in in_node:
                root.val = num


        def dfs(node):
            if not child_list[node.val]:
                return None
            for child_node, isLeft in child_list[node.val]:
                if isLeft:
                    node.left = TreeNode(child_node)
                    dfs(node.left)
                else:
                    node.right = TreeNode(child_node)
                    dfs(node.right)

        dfs(root)

        return root