class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        result = []
        
        def backtrack(s, path):

            if not s and len(path) >= 3:
                result.append(path)
                return True
            for i in range(1, len(s) + 1):
                current = s[:i]
                if not self.is_valid(current, path):
                    continue
                if backtrack(s[i:], path + [int(current)]):
                    return True
            return False

        backtrack(num, [])
        return len(result) > 0

    def is_valid(self, s, path):
        if len(s) > 1 and s[0] == '0':
            return False
        return len(path) < 2 or (path[-1] + path[-2] == int(s))