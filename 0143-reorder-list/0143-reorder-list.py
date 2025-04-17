# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        second_list = slow

        while second_list:
            tmp = second_list.next
            second_list.next = prev
            prev = second_list
            second_list = tmp

        first, second = head, prev
        while second.next:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2
