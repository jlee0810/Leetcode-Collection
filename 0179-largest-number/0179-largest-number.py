class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        string_nums = [str(num) for num in nums]
        string_nums.sort(key = lambda a : a * 10, reverse = True)
        if string_nums[0] == '0':
            return "0"
        else:
            return "".join(string_nums)