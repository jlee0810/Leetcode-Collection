class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #backtracking
        result = []

        def backtrack(nums, permutation):
            if len(nums) == 0:
                result.append(permutation.copy())
                return
            for n in nums:
                nums_copy = nums.copy()
                num = nums_copy.pop(nums_copy.index(n))
                permutation.append(num)
                backtrack(nums_copy, permutation)
                permutation.pop()
        backtrack(nums, [])
        return result