class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        min_idx = max_idx = 0
        min = float('inf') 
        max = float('-inf')
        for i in range(len(nums)):
            if nums[i] < min:
                min_idx = i
                min = nums[i]
            if nums[i] >= max:
                max_idx = i
                max = nums[i]
            
        result = (min_idx + len(nums) - 1 - max_idx) if min_idx < max_idx else (min_idx + len(nums) -2 - max_idx)

        return result