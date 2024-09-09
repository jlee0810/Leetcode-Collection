class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix = {}
        
        max_length = 0
        zero_count = 0
        one_count = 0

        prefix[0] = -1
        
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
            else:
                one_count += 1
            
            diff = zero_count - one_count
            
            if diff in prefix:
                max_length = max(max_length, i - prefix[diff])
            else:
                prefix[diff] = i
        
        return max_length
