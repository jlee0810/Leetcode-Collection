class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not len(digits):
            return []

        map = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}

        result = []

        def backtrack(start, combo):
            if len(combo) == len(digits):
                result.append(combo)
                return
            for i in range(len(map[digits[start]])):
                combo += map[digits[start]][i]
                backtrack(start + 1, combo)
                combo = combo[:len(combo) - 1]

        backtrack(0, '')
        return result