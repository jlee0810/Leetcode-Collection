class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        min_heap = list(count.keys())
        heapify(min_heap)

        while min_heap:
            top = min_heap[0]

            for i in range(groupSize):
                curr = top + i
                if curr not in count:
                    return False
                count[curr] -= 1

                if count[curr] == 0:
                    if min_heap[0] != curr:
                        return False
                    else:
                        heappop(min_heap)
        return True
