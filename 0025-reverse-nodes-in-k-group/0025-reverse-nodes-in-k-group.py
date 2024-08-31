# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def kth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = group_prev = ListNode(0, head)

        while True:
            kth = self.kth(group_prev, k)
            if not kth:
                break

            group_prev.next = kth
            group_next = kth.next

            prev, curr = group_next, head
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            group_prev = head
            head = group_next

        return dummy.next