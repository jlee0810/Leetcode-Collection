class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        count = 0
        total_sum = sum(nums)
        first_part = 0
        for i in range(len(nums) - 1):
            first_part += nums[i]
            second_part = total_sum - first_part
            if first_part >= second_part:
                count += 1
        
        return count