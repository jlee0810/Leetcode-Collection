class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(arr)
        arr.sort()
        dp = [1 for _ in range(n)]

        index = {x : i for i, x in enumerate(arr)}

        for i, x in enumerate(arr):
            for j in range(i):
                if x % arr[j] == 0:
                    right = x // arr[j]
                    if right in index:
                        dp[i] += dp[j] * dp[index[right]]
                        dp[i] %= mod

        return sum(dp) % mod