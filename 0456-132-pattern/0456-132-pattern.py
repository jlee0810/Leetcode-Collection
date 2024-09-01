class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        length = len(nums)

        if length < 3:
            return False

        strict_decrease = []
        max_third_num = float('-inf')

        for i in range(length - 1, -1, -1):
            if nums[i] < max_third_num:
                return True
            
            while strict_decrease and strict_decrease[-1] < nums[i]:
                max_third_num = strict_decrease.pop()

            strict_decrease.append(nums[i])

        return False