class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]

        current_total = 0
        for n in nums:
            current_total += n
            result = max(result, current_total)
            if current_total < 0:
                current_total = 0

        return result