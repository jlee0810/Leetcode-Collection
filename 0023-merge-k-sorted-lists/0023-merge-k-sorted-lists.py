# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        dummy = ListNode()
        cnt = 0

        for lst in lists:
            if lst:
                heappush(min_heap, [lst.val, cnt, lst])
            cnt += 1

        curr = dummy
        while min_heap:
            curr_val, _, curr_lst = heappop(min_heap)
            curr.next = curr_lst
            curr = curr.next
            
            if curr_lst.next:
                heappush(min_heap, [curr_lst.next.val, cnt, curr_lst.next])
                cnt += 1
            
        return dummy.next