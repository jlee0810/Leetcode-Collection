class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #DP O(n^2)
        # dp = [False for _ in range(len(nums))]
        # dp[-1] = True

        # for i in range(len(nums) -2, -1, -1):
        #     maxJump = nums[i]
        #     for j in range(maxJump + 1):
        #         if i + j < len(nums) and dp[i + j]:
        #             dp[i] = True
        # return dp[0]

        #Greedy O(n)
        lastIdx = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= lastIdx:
                lastIdx = i
        return lastIdx == 0