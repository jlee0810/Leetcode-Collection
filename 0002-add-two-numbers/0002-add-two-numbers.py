class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_head = l1
        l2_head = l2

        dummy = ListNode()
        current = dummy
        carry = 0
        
        while l1_head or l2_head:
            x = l1_head.val if l1_head else 0
            y = l2_head.val if l2_head else 0

            sum = x + y + carry

            carry = sum // 10
            current.next = ListNode(sum % 10)
            current = current.next
            if l1_head:
                l1_head = l1_head.next
            if l2_head:
                l2_head = l2_head.next

        if carry:
            current.next = ListNode(carry)

        return dummy.next
