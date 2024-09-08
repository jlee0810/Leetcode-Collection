class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        cnt = Counter(hand)
        min_heap = heapify(list(cnt.keys()))

        while min_heap:
            top = min_heap[0]
            for i in range(1, groupSize):
                curr = top + i
                if curr not in cnt:
                    return False
                cnt[curr] -= 1
                if cnt[curr] == 0:
                    if min_heap[0] != curr:
                        return False
                    else:
                        heappop(min_heap)
        return True