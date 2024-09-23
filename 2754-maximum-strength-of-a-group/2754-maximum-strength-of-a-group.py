class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        positives = []
        negatives = []
        zero_count = 0
        
        for num in nums:
            if num > 0:
                positives.append(num)
            elif num < 0:
                negatives.append(num)
            else:
                zero_count += 1
        
        negatives.sort()
        
        if len(negatives) % 2 != 0:
            negatives.pop()
        
        strength = 1
        for num in positives + negatives:
            strength *= num
        
        if strength == 1 and not positives and not negatives:
            return 0
        
        return strength
