class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[n - 1] = 0

        for i in range(n - 2, -1, -1):
            max_jump = min(i + nums[i], n - 1)
            for j in range(i + 1, max_jump + 1):
                dp[i] = min(dp[i], dp[j] + 1)
                if dp[i] == 1:
                    break
        return dp[0]