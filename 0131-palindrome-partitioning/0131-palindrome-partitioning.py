class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def check_pal(str):
            l, r = 0, len(str) - 1
            while l <= r:
                if str[l] != str[r]:
                    return False
                else:
                    l += 1
                    r -= 1
            return True
        
        result = []

        def backtrack(idx, combo):
            nonlocal result
            if idx == len(s):
                result.append(combo.copy())
                return
            for i in range(idx, len(s)):
                if check_pal(s[idx : i + 1]):
                    combo.append(s[idx : i + 1])
                    backtrack(i + 1, combo)
                    combo.pop()
        
        backtrack(0, [])
        return result