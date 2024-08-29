class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x, y):
            return sqrt(x ** 2 + y ** 2)

        min_heap = []

        for x, y in points:
            heappush(min_heap, (distance(x, y), x, y))
                
        result = []

        while k > 0:
            distance, curr_x, curr_y = heappop(min_heap)
            result.append([curr_x, curr_y])
            k -= 1

        return result