# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        min_heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))

        while min_heap:
            curr_val, i, curr_node = heapq.heappop(min_heap)
            curr.next = curr_node
            curr = curr.next

            if curr_node.next:
                heapq.heappush(min_heap, (curr_node.next.val, i, curr_node.next))

        return dummy.next