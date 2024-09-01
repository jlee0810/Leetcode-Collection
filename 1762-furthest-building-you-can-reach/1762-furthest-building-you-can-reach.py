class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        min_heap = []

        for i in range(1, len(heights)):
            climb = heights[i] - heights[i - 1]

            if climb < 0:
                continue

            heappush(min_heap, climb)

            if len(min_heap) <= ladders:
                continue
            
            min_climb = heappop(min_heap)
            bricks -= min_climb
            if bricks < 0:
                return i - 1
            
        return len(heights) - 1