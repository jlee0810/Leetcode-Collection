class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        for num in nums:
            heappush(max_heap, -num)
        
        result = []
        for _ in range(k):
            result.append(heappop(max_heap) * - 1)
        return result[-1]