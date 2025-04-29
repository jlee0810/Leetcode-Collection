# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class HeapNode:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []

        for lst in lists:
            if lst:
                heappush(minHeap, HeapNode(lst))

        dummy = ListNode()

        curr = dummy

        while minHeap:
            currNode = heappop(minHeap)
            currNode = currNode.node

            if currNode.next:
                heappush(minHeap, HeapNode(currNode.next))
            curr.next = currNode
            curr = curr.next

        return dummy.next
