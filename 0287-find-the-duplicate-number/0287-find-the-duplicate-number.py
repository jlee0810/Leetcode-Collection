class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        dup_idx = 0

        while dup_idx != slow:
            dup_idx = nums[dup_idx]
            slow = nums[slow]

        return dup_idx
