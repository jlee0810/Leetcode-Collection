class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(idx, combo):
            if (len(combo) == k):
                result.append(combo.copy())
                return
            for i in range(idx, n + 1):
                combo.append(i)
                backtrack(i + 1, combo)
                combo.pop()

        backtrack(1, [])
        return result