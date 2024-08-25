class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(idx, subset):
            result.append(subset.copy())
            prev = -1000
            for i in range(idx, len(nums)):
                if nums[i] == prev:
                    continue
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()
                prev = nums[i]
        
        backtrack(0, [])
        return result