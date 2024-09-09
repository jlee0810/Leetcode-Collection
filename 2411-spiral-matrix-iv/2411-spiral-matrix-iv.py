# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: "ListNode") -> List[List[int]]:
        i = 0
        j = 0
        curr_d = 0
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        result = [[-1 for _ in range(n)] for _ in range(m)]

        while head is not None:
            result[i][j] = head.val
            new_i = i + direction[curr_d][0]
            new_j = j + direction[curr_d][1]

            if (min(new_i, new_j) < 0 or new_i >= m or new_j >= n or result[new_i][new_j] != -1):
                curr_d = (curr_d + 1) % 4
            i += direction[curr_d][0]
            j += direction[curr_d][1]

            head = head.next

        return result