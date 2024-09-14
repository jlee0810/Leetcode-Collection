class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        max_width = 0
        mono_stack = []

        for i in range(len(nums)):
            if not mono_stack or nums[mono_stack[-1]] > nums[i]:
                mono_stack.append(i)

        for i in range(len(nums) - 1, -1, -1):
            while mono_stack and nums[mono_stack[-1]] <= nums[i]:
                max_width = max(max_width, i - mono_stack.pop())
        
        return max_width