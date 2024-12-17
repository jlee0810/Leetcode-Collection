class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(idx, ss):
            if idx == len(nums):
                result.append(ss.copy())
                return
            ss.append(nums[idx])
            backtrack(idx + 1, ss)
            ss.pop()
            while idx + 1 < len(nums) and nums[idx  + 1] == nums[idx]:
                idx += 1
            backtrack(idx + 1, ss)

        backtrack(0, [])
        return result