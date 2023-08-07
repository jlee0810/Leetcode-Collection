class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for x, y in points:
            distance = x ** 2 + y ** 2
            heappush(minHeap, (distance, x, y))
        result = []
        while k > 0:
            result.append([minHeap[0][1], minHeap[0][2]])
            heappop(minHeap)
            k -= 1
        return result
