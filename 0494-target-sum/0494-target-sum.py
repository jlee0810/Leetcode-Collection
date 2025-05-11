class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def dp(i, curr_sum):
            if (i, curr_sum) in cache:
                return cache[(i, curr_sum)]
            if i == len(nums) and curr_sum == target:
                return 1
            if i == len(nums):
                return 0

            add_way = dp(i + 1, curr_sum + nums[i])
            subtract_way = dp(i + 1, curr_sum - nums[i])

            cache[(i, curr_sum)] = add_way + subtract_way

            return add_way + subtract_way

        return dp(0, 0)
