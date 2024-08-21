class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        count = 0

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                sub_arr = nums[i : j + 1]
                count += len(set(sub_arr)) ** 2
        return count
        