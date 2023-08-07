# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #First Attempt Min Heap
        # minHeap = []

        # def dfs(node):
        #     if not node:
        #         return 
        #     heappush(minHeap, node.val)
        #     dfs(node.left)
        #     dfs(node.right)
        # dfs(root)
        
        # for _ in range(k - 1):
        #     heappop(minHeap)
        # return minHeap[0]


        #Second Method In Order Traversal
        def inOrder(root):
            nonlocal k
            if root and k > 0:
                inOrder(root.left)

                # decrement k each time you find a value
                k -= 1
                if k == 0:
                    self.result = root.val

                # continue to recur on the right child
                inOrder(root.right)

        self.result = None
        inOrder(root)
        return self.result





