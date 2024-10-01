class Solution:
    def decodeString(self, s: str) -> str:
        def recurse(idx):
            count = 0
            decoded = []

            while idx < len(s):
                if s[idx].isdigit():
                    count = count * 10 + int(s[idx])
                    idx += 1
                elif s[idx] == '[':
                    substr, idx = recurse(idx + 1)
                    decoded.append(substr * count)
                    count = 0
                elif s[idx] == ']':
                    return "".join(decoded), idx + 1
                else:
                    decoded.append(s[idx])
                    idx += 1
            
            return "".join(decoded)
        return recurse(0)