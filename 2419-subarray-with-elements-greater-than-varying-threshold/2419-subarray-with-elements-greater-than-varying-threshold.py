class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        left = [-1 for _ in range(len(nums))]
        right = [len(nums) for _ in range(len(nums))]

        stack = []

        for idx in range(len(nums)):
            while stack and nums[stack[-1]] >= nums[idx]:
                stack.pop()
            if stack:
                left[idx] = stack[-1]
            stack.append(idx)

        stack = []

        for idx in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[idx]:
                stack.pop()
            if stack:
                right[idx] = stack[-1]
            stack.append(idx)
        
        for i in range(len(nums)):
            k = right[i] - left[i] - 1
            if nums[i] > threshold / k:
                return k

 
        return -1
        