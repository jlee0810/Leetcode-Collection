class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        @lru_cache
        def dp(i, j):
            if i == j:
                return 0
            min_cost = float('inf')
            for k in range(i, j):
                left_max = max(arr[i : k + 1])
                right_max = max(arr[k + 1 : j + 1])
                cost = dp(i, k) + dp(k + 1, j) + left_max * right_max
                min_cost = min(min_cost, cost)
            return min_cost
        
        return dp(0, len(arr) - 1)