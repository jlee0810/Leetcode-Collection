class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        list_val = []
        node_dict = defaultdict(set)

        curr = head
        while curr:
            list_val.append(curr.val)
            node_dict[curr.val].add(curr)
            curr = curr.next
        
        list_val.sort()

        dummy = ListNode(0)
        curr = dummy
        for num in list_val:
            node = node_dict[num].pop()
            curr.next = node
            curr = curr.next
        
        curr.next = None

        return dummy.next
