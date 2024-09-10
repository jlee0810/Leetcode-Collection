# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        nxt = head.next

        while nxt:
            gcd = math.gcd(curr.val, nxt.val)
            new = ListNode(gcd, nxt)
            curr.next = new
            curr = nxt
            nxt = nxt.next

        return head 