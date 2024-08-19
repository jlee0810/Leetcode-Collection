class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        if any(len(s) == 0 for s in strs):
            return ""
        
        index = 0

        while True:
            if index >= len(strs[0]):
                break

            char = strs[0][index]

            if all(index < len(s) and s[index] == char for s in strs):
                index += 1
            else:
                break

        return strs[0][:index]
