class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def backtrack(idx, subset):
            if idx == len(nums):
                result.append(subset.copy())
                return
            
            for bool in [True, False]:
                if bool:
                    subset.append(nums[idx])
                    backtrack(idx + 1, subset)
                    subset.pop()
                else:
                    while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                        idx += 1
                    backtrack(idx + 1, subset)
            
        backtrack(0, [])
        return result