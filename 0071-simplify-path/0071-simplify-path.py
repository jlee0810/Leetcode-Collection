class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = [part for part in path.split('/') if part]
        stack = []

        for part in parts:
            if part == '.':
                continue
            elif part == '..':
                if not stack:
                    continue
                stack.pop()
            else:
                stack.append(part)
        result = '/'
        result += '/'.join(stack)

        return result