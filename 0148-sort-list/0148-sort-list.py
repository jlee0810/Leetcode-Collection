# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode()
        node_dict = defaultdict(list)
        lst = []
        curr = head

        while curr:
            node_dict[curr.val].append(curr) 
            lst.append(curr.val)
            curr = curr.next

        lst.sort()

        curr = dummy
        for num in lst:
            node = node_dict[num].pop(0)
            curr.next = node
            curr = curr.next
        
        curr.next = None
        
        return dummy.next