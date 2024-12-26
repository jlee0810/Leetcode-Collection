class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = ""
        s_ptr = 0

        for i, c in enumerate(s):
            if s_ptr == len(spaces):
                result += s[i : ]
                break
            if i == spaces[s_ptr]:
                result += ' '
                s_ptr += 1
            result += s[i]

        return result