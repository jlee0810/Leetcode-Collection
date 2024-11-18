class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []


        def backtrack(idx, sset):
            if idx == len(nums):
                result.append(sset.copy())
                return
            sset.append(nums[idx])
            backtrack(idx + 1, sset)
            sset.pop()
            backtrack(idx + 1, sset)
        
        backtrack(0, [])

        return result
