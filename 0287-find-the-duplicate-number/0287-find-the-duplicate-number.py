class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        turtle = nums[0]
        hare = nums[nums[0]]

        while turtle != hare:
            turtle = nums[turtle]
            hare = nums[nums[hare]]
        
        slow = 0

        while slow != turtle:
            slow = nums[slow]
            turtle = nums[turtle]

        return slow