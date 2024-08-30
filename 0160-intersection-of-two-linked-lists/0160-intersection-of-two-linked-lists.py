# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        point_A = headA
        point_B = headB

        while point_A != point_B:
            point_A = headB if point_A is None else point_A.next
            point_B = headA if point_B is None else point_B.next
        
        return point_A
        # s = set()

        # while headA:
        #     s.add(headA)
        #     headA = headA.next

        # while headB:
        #     if headB in s:
        #         return headB
        #     headB = headB.next
        
        