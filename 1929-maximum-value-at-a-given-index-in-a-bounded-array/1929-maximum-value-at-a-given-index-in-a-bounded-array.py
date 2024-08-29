class Solution:
    def getSum(self, index: int, value: int, n: int) -> int:
        count = 0
        if value > index:
            count += (value + value - index) * (index + 1) // 2
        else:
            count += (value + 1) * value // 2 + index - value + 1
        
        if value >= n - index:
            count += (value + value - n + 1 + index) * (n - index) // 2
        else:
            count += (value + 1) * value // 2 + n - index - value
        
        return count - value
        # curr_sum = 0

        # left_val = value - 1

        # for i in range(index -1, -1, -1):
        #     if left_val <= 0:
        #         left_val = 1
        #     curr_sum += left_val
        #     left_val -= 1
        
        # right_val = value - 1
        # for i in range(index + 1, n):
        #     if right_val <= 0:
        #         right_val = 1
        #     curr_sum += right_val
        #     right_val -= 1
        
        # return curr_sum + value

    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left, right = 1, maxSum
        while left < right:
            mid = (left + right + 1) // 2
            if self.getSum(index, mid, n) <= maxSum:
                left = mid
            else:
                right = mid - 1
        
        return left
