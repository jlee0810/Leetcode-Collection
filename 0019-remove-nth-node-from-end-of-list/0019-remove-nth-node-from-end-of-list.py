# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head
        dummy = ListNode()
        dummy.next = head

        while n - 1 > 0:
            fast = fast.next
            n -= 1

        prev = dummy
        while fast.next:
            fast = fast.next
            prev = slow
            slow = slow.next

        if slow:
            prev.next = slow.next
        else:
            prev.next = None

        return dummy.next
