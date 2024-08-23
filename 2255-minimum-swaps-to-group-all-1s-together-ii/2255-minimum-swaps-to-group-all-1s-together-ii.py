class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        num_ones = nums.count(1)
        orig_len = len(nums)
        nums = nums + nums
        
        if num_ones == 0:
            return 0

        window_count = 0
        min_swap = float('inf')

        l = 0
  
        for r in range(orig_len + num_ones - 1):
            if nums[r] == 1:
                window_count += 1
            if r >= num_ones:
                if nums[l] == 1:
                    window_count -= 1
                l += 1
            min_swap = min(min_swap, num_ones - window_count)

        return min_swap