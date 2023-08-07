
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        leftLess, rightLEQ = [-1] * n, [n] * n
        leftG, rightGEQ = [-1] * n, [n] * n 
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                index = stack.pop()
                rightLEQ[index] = i
            stack.append(i)
        
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] > nums[i]:
                index = stack.pop()
                leftLess[index] = i
            stack.append(i)

        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] <= nums[i]:
                index = stack.pop()
                rightGEQ[index] = i
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                index = stack.pop()
                leftG[index] = i
            stack.append(i)
        res = 0
        for i in range(n):
            res += (((rightGEQ[i] - i) * (i - leftG[i])) - ((rightLEQ[i] - i) * (i - leftLess[i]))) * nums[i]
        return res