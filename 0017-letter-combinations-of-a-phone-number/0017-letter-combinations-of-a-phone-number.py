class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        charNum = {'2': ['a', 'b', 'c'], '3' : ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q','r', 's'], '8': ['t', 'u', 'v'], '9': ['w','x', 'y','z']}

        result = []

        if not digits:
            return None

        def backtrack(idx, combo):
            if idx == len(digits):
                result.append(combo)
                return
            for c in charNum[digits[idx]]:
                combo += c
                backtrack(idx + 1, combo)
                combo = combo[:-1]
        
        backtrack(0, "")

        return result