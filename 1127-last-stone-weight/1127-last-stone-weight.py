class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []   

        for stone in stones:
            heappush(max_heap, stone * - 1)

        while len(max_heap) > 1:
            first = heappop(max_heap) * -1
            second = heappop(max_heap) * -1
            
            if first == second:
                continue
            else:
                heappush(max_heap, -abs(first - second))

        return max_heap[0] * -1 if max_heap else 0
