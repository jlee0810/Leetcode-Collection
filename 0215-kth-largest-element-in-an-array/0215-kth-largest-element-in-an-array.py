class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        for num in nums:
            heappush(max_heap, -num)

        kth = None
        while k > 0:
            kth = heappop(max_heap) * -1
            k -= 1
        return kth
            