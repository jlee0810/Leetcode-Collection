class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'}': '{', ")" : '(', ']' : '['}

        for c in s:
            if c in pairs:
                if not stack or stack[-1] != pairs[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        
        return len(stack) == 0

        