class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_result = max(nums)
        curr_min = 1
        curr_max = 1

        for num in nums:
            if num == 0:
                curr_min = 1
                curr_max = 1
                continue
            temp = curr_min
            curr_min = min(num, curr_min * num, curr_max * num)
            curr_max = max(num, temp * num, curr_max * num)
            max_result = max(max_result, curr_max)

        return max_result