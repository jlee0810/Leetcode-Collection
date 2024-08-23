class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            if curr.val < 0 and prev is not None:
                node = curr
                prev.next = curr.next
                curr = curr.next
                
                node.next = head
                head = node  
            else:
                prev = curr
                curr = curr.next

        return head