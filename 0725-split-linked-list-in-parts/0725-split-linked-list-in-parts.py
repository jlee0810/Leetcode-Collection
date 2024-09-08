class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        list_length = length // k
        extra = length - list_length * k 

        result = []

        for _ in range(k):
            dummy = ListNode(0, head)
            curr = head
            curr_length = list_length + (1 if extra > 0 else 0)
            extra -= 1

            curr_length -= 1

            while curr_length > 0:
                curr = curr.next
                curr_length -= 1

            if curr:
                head = curr.next
                curr.next = None
            result.append(dummy.next)
            
        return result