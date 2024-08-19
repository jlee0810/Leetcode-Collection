# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        target = head
        target_prev = None
        curr = head

        n -= 1
        while n:
            n -= 1
            curr = curr.next

        while curr.next:
            curr = curr.next
            target_prev = target
            target = target.next

        if not target_prev and curr == target:
            return None
        elif not target_prev:
            return head.next
        target_prev.next = target.next

        return head
