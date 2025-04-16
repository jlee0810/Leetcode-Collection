# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_kth(self, node, k):
        while k > 0 and node:
            node = node.next
            k -= 1
        return node

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        groupPrev = dummy

        while True:
            kth = self.get_kth(groupPrev, k)
            if not kth:
                break
            curr = groupPrev.next

            prev = kth.next
            groupNext = kth.next

            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        
        return dummy.next