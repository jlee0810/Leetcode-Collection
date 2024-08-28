class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        s = None
        ops = 0
        
        while len(nums) >= 2:
            if s is None:
                s = nums[0] + nums[1]
            else:
                if s != nums[0] + nums[1]:
                    break
            ops += 1
            nums = nums[2:]
        
        return ops