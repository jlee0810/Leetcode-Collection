class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        min_heap = []

        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]

            if climb <= 0:
                continue
            
            heappush(min_heap, climb)

            if len(min_heap) <= ladders:
                continue
            
            min_jump = heappop(min_heap)
            bricks -= min_jump
            if bricks < 0:
                return i
        
        return len(heights) - 1