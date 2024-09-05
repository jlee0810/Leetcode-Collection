class Solution:
    def minSteps(self, n: int) -> int:
        result = float('inf')
        
        def backtrack(curr_len, curr_memory, last_copy, count):
            nonlocal result
            if curr_len == n:
                result = min(result, count)
                return 
            if curr_len > n:
                return
            if not last_copy:
                backtrack(curr_len, curr_len, True, count + 1)
            if curr_memory > 0:
                backtrack(curr_len + curr_memory, curr_memory, False, count + 1)

        backtrack(1, 0, False, 0)

        return result