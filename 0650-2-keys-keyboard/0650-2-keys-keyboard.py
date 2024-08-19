class Solution:
    def minSteps(self, n: int) -> int:
        result = float('inf')

        @lru_cache
        def backtrack(curr_len, curr_memory, curr_count, last_move_copy):
            nonlocal result
            if curr_len == n:
                result = min(result, curr_count)
                return
            if curr_len > n:
                return
            
            if not last_move_copy:
                backtrack(curr_len, curr_len, curr_count + 1, True)
            
            if curr_memory > 0:
                backtrack(curr_len + curr_memory, curr_memory, curr_count + 1, False)
        
        backtrack(1, 0, 0, False)

        return result
