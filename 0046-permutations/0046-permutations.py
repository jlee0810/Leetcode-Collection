class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(remain, permutation):
            if len(remain) == 0:
                result.append(permutation.copy())
                return
            
            for i in range(len(remain)):
                permutation.append(remain[i])
                newNum = remain[:i] + remain[i + 1 : ]
                backtrack(newNum, permutation)
                permutation.pop()
        backtrack(nums, [])
        return result