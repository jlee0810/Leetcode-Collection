class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
    
        n = len(nums)
        dp = [[1, 1] for _ in range(n)]
    
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i][0] = max(dp[i][0], dp[j][1] + 1)
                elif nums[i] < nums[j]:
                    dp[i][1] = max(dp[i][1], dp[j][0] + 1)
        return max(dp[-1][0], dp[-1][1])
    