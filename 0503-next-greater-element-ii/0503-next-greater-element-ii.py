class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [0] * length


        max_num = max(nums)
        indicies_of_max = []
        for idx, num in enumerate(nums):
            if num == max_num:
                indicies_of_max.append(idx)
        for idx in indicies_of_max:
            result[idx] = -1

        nums = nums + nums

        mono_stack = []
        for idx, num in enumerate(nums):
            while mono_stack and num > nums[mono_stack[-1]]:
                result[mono_stack.pop()] = num
            if idx < length:
                mono_stack.append(idx)
        return result