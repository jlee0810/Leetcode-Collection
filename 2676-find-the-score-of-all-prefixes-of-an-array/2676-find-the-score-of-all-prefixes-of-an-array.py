class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        max_prefix = [0 for _ in range(len(nums))]
        max_so_far = 0
        for idx, num in enumerate(nums):
            max_prefix[idx] = max(max_so_far, num)
            max_so_far = max(max_so_far, num)
        
        conver = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            conver[i] = (conver[i - 1] + nums[i] + max_prefix[i])
        
        return conver