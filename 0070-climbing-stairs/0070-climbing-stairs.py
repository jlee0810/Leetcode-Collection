class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {0: 1, 1: 1, 2: 2}

        def dp(i):
            if i in cache:
                return cache[i]
            cache[i] = dp(i - 1) + dp(i - 2)
            return cache[i]

        return dp(n)
