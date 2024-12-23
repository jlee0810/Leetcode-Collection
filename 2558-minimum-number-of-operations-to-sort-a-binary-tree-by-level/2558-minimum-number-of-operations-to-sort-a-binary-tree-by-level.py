# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)

        total = 0
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            swap = self.min_swaps_to_sort(level)
            total += swap

        return total

    def min_swaps_to_sort(self, original):
        swaps = 0
        target = sorted(original)

        pos = {val: idx for idx, val in enumerate(original)}

        for i in range(len(original)):
            if original[i] != target[i]:
                swaps += 1

                cur_pos = pos[target[i]]
                pos[original[i]] = cur_pos
                original[cur_pos] = original[i]

        return swaps