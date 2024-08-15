class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x, y):
            return sqrt(x ** 2 + y ** 2)

        min_heap = []

        for x, y in points:
            heappush(min_heap, (distance(x, y), x, y))
                
        result = []

        for _ in range(k):
            curr_point = heappop(min_heap)
            result.append([curr_point[1], curr_point[2]])
        
        return result