class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_accum = 1
        right_accum = 1

        result = [1 for _ in range(len(nums))]
        
        for i in range(len(nums)):
            result[i] *= left_accum
            left_accum *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            result[i] *= right_accum
            right_accum *= nums[i]

        return result