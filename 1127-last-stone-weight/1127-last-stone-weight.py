class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for stone in stones:
            heappush(max_heap, stone * -1)
        
        while len(max_heap) > 1:
            first = heappop(max_heap) * -1
            second = heappop(max_heap) * -1

            if first == second:
                continue
            else:
                diff = first - second
                heappush(max_heap, diff * -1)
        
        return max_heap[0] * -1 if len(max_heap) else 0

