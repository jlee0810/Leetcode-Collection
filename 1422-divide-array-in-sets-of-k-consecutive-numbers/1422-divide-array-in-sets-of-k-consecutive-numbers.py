class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        cnt = Counter(nums)
        min_heap = list(cnt.keys())
        heapq.heapify(min_heap)

        while min_heap:
            top = min_heap[0]
            for i in range(k):
                curr_num = top + i
                if cnt[curr_num] == 0:
                    return False
                cnt[curr_num] -= 1
                if cnt[curr_num] == 0:
                    if curr_num != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)
        
        return True