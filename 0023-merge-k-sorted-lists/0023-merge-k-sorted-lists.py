# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists):
        dummy = ListNode()
        curr = dummy

        min_heap = []
        
        counter = 0
        for node in lists:
            if node:
               heappush(min_heap, (node.val, counter, node))
               counter += 1
        
        while min_heap:
            curr_val, counter, curr_node = heapq.heappop(min_heap)
            curr.next = curr_node
            curr = curr.next

            if curr_node.next:
                heapq.heappush(min_heap, (curr_node.next.val, counter, curr_node.next))

        return dummy.next