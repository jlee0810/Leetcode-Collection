# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr 
    
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = groupPrev = ListNode(0, head)

        while True:
            kth = self.getKth(groupPrev, k)
            
            if not kth:
                break

            groupPrev.next = kth
            groupNext = kth.next

            prev, curr = groupNext, head
            while curr != groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            groupPrev = head
            head = groupNext
        return dummy.next