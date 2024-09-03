class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i == j:
                return 0

            min_sum = float('inf')
            for k in range(i, j):
                left_max = max(arr[i : k + 1])
                right_max = max(arr[k + 1 : j + 1])
                curr_sum = dp(i, k) + dp(k + 1, j) + left_max * right_max
                min_sum = min(min_sum, curr_sum)

            return min_sum
        
        return dp(0, len(arr) - 1)