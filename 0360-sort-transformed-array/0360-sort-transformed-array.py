class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        #Easy solution O(nlogn)
        # def fn(num):
        #     return a * (num ** 2) + b * num + c
        # result = []

        # for num in nums:
        #     result.append(fn(num))

        # result.sort()
        # return result

        #Take advantage of quadratic equation characteristic
        def fn(num):
            return a * (num ** 2) + b * num + c

        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1

        if a > 0:
            idx = n - 1
            while left <= right:
                left_val, right_val = fn(nums[left]), fn(nums[right])
                if left_val > right_val:
                    result[idx] = left_val
                    left += 1
                else:
                    result[idx] = right_val
                    right -= 1
                idx -= 1
        else:
            idx = 0
            while left <= right:
                left_val, right_val = fn(nums[left]), fn(nums[right])
                if left_val < right_val:
                    result[idx] = left_val
                    left += 1
                else:
                    result[idx] = right_val
                    right -= 1
                idx += 1

        return result
