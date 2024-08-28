class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapify(nums)
        self.min_heap = nums

        while len(self.min_heap) > k:
            heappop(self.min_heap)

    def add(self, val: int) -> int:
        heappush(self.min_heap, val)

        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]

        heappush()

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)