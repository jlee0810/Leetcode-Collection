class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_result = float('-inf')
        curr_sum = 0

        for num in nums:
            curr_sum += num
            max_result = max(curr_sum, max_result)
            if curr_sum < 0:
                curr_sum = 0
        return max_result

