class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum(num for num in nums if num % 2 == 0)
        result = []
        
        for add, idx in queries:
            original_num = nums[idx]
            
            if original_num % 2 == 0:
                even_sum -= original_num
            
            nums[idx] += add
            new_num = nums[idx]
            
            if new_num % 2 == 0:
                even_sum += new_num
            
            result.append(even_sum)

        return result