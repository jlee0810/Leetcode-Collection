class Solution:
    def maxLength(self, arr: List[str]) -> int:
        result = 0

        def backtrack(idx, string_formed):
            nonlocal result
            if len(string_formed) == len(set(string_formed)):
                result = max(result, len(string_formed))

            if idx == len(arr):
                return

            for i in range(idx, len(arr)):
                new_string_formed = string_formed + arr[i]
                backtrack(i + 1, new_string_formed)
                
        backtrack(0, '')
        return result
