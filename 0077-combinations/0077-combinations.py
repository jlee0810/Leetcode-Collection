class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(start, combination):
            if len(combination) == k:
                result.append(combination.copy())
                return
            for i in range(start, n + 1):
                combination.append(i)
                dfs(i + 1, combination)
                combination.pop()
        dfs(1, [])
        return result
