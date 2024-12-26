class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def backtrack(idx, current_sum):
            if (idx, current_sum) in cache:
                return cache[(idx, current_sum)]

            if idx == len(nums):
                return 1 if current_sum == target else 0

            add = backtrack(idx + 1, current_sum + nums[idx])
            subtract = backtrack(idx + 1, current_sum - nums[idx])
            
            cache[(idx, current_sum)] = add + subtract
            return cache[(idx, current_sum)]
        
        return backtrack(0, 0)