class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        stack = []
        sum_of_minimums = 0

        for i in range(len(arr) + 1):
            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):
                mid = stack.pop()
                left_bound = -1 if not stack else stack[-1]
                right_bound = i
                count = (mid - left_bound) * (right_bound - mid)
                sum_of_minimums += (count * arr[mid])
            stack.append(i)
        
        return sum_of_minimums % MOD