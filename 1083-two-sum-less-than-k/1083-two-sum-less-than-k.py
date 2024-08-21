class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_sum = -1

        l, r = 0, len(nums) - 1

        while l < r:
            current_sum = nums[l] + nums[r]
        
            if current_sum < k:
                l += 1
                max_sum = max(max_sum, current_sum)
            else:
                r -= 1
            
            

        return max_sum