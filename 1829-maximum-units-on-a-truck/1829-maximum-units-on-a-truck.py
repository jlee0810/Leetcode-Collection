class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        max_heap = []

        for count, unit in boxTypes:
            for _ in range(count):
                heappush(max_heap, -unit)
        total = 0
        while max_heap and truckSize > 0:
            unit = heappop(max_heap) * -1
            total += unit
            truckSize -= 1
        
        return total