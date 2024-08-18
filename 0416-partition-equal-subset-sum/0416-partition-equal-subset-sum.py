class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        dp = set()
        dp.add(0)

        half = sum(nums) // 2

        for i in range(len(nums)):
            newDP = set()
            for num in dp:
                if nums[i] + num == half:
                    return True
                newDP.add(num)
                newDP.add(nums[i] + num)
            dp = newDP
        
        return False