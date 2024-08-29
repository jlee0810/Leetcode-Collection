class Solution:
    def decodeString(self, s: str) -> str:
        def recurse(idx):
            count = 0
            decoded = []

            while idx < len(s):
                if s[idx].isnumeric():
                    count = count * 10 + int(s[idx])
                    idx += 1
                elif s[idx] == '[':
                    substring, idx = recurse(idx + 1)
                    substring *= count
                    decoded.append(substring)
                    count = 0
                elif s[idx] == ']':
                    compile_string = ''.join(decoded)
                    return compile_string, idx + 1
                else:
                    decoded.append(s[idx])
                    idx += 1
        
            return "".join(decoded)

        return recurse(0)

