class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        visited = [False for _ in range(len(nums))]

        def backtrack(permute):
            if len(permute) == len(nums):
                result.append(permute.copy())
                return
            for i in range(len(visited)):
                if visited[i]:
                    continue
                visited[i] = True
                permute.append(nums[i])
                backtrack(permute)
                visited[i] = False
                permute.pop()

        backtrack([])

        return result