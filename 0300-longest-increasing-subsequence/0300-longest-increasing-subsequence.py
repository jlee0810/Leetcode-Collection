class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        max_length = [0 for _ in range(len(nums))]

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    max_length[i] = max(max_length[i], max_length[j] + 1)
        return max(max_length) + 1