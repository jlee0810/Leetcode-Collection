class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        
        k_largest = heapq.nlargest(k, indexed_nums, key=lambda x: x[0])
        
        k_largest_sorted_by_index = sorted(k_largest, key=lambda x: x[1])
        
        result = [num for num, _ in k_largest_sorted_by_index]
        
        return result
