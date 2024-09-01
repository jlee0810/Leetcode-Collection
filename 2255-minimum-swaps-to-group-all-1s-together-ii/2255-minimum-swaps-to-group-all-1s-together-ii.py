class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        circular = nums + nums

        num_ones = sum(nums)
        l, r = 0, 0

        min_swap = float('inf')

        window_ones = 0
        
        while r < len(circular):
            window_ones += circular[r]
            
            if r - l + 1 == num_ones:
                current_swap = num_ones - window_ones
                min_swap = min(min_swap, current_swap)
                window_ones -= circular[l]
                l += 1

            r += 1

        if min_swap == float('inf'):
            return 0
        return min_swap