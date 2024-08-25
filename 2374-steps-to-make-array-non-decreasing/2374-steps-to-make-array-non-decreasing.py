class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stack = []
        max_steps = 0

        for num in nums:
            current_step = 0

            while stack and stack[-1][0] <= num:
                current_step = max(current_step, stack.pop()[1])
            
            if stack:
                current_step += 1
            
            max_steps = max(max_steps, current_step)
            
            stack.append((num, current_step))
        
        return max_steps
