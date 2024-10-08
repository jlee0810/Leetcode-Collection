# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        count = 0

        for lst in lists:
            if lst:
                heappush(min_heap, (lst.val, count, lst))
                count += 1
        
        dummy = ListNode()
        curr = dummy

        while min_heap:
            _, _, node = heappop(min_heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heappush(min_heap, (node.next.val, count, node.next))
            count += 1
        
        return dummy.next