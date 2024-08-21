class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        max_heap = []
        cnt = Counter()
        
        result = []

        for num, f in zip(nums, freq): 
            cnt[num] += f
            while max_heap and cnt[max_heap[0][1]] + max_heap[0][0] != 0:
                heappop(max_heap)
                
            heappush(max_heap, (-cnt[num], num))
            result.append(-max_heap[0][0])

        return result 