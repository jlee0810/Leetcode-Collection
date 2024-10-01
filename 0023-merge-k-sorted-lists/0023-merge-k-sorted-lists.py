# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        min_heap = []

        counter = 0
        for lst in lists:
            if lst:
                heappush(min_heap, (lst.val, counter, lst))
                counter += 1

        curr = dummy

        while min_heap:
            _, _, curr_node = heappop(min_heap)
            curr.next = curr_node
            if curr_node.next:
                heappush(min_heap, (curr_node.next.val, counter, curr_node.next))
                counter += 1
            curr = curr.next

        return dummy.next
        