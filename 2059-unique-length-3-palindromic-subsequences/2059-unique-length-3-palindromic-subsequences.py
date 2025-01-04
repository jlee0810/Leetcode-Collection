class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = [-1] * 26
        last = [-1] * 26

        for i in range(len(s)):
            curr = ord(s[i]) - ord("a")
            if first[curr] == -1:
                first[curr] = i

            last[curr] = i

        result = 0
        s_char = set(s)

        for c in s_char:
            first_idx, last_idx = first[ord(c) - ord("a")], last[ord(c) - ord("a")]
            middle_char = set()
            for i in range(first_idx + 1, last_idx):
                if s[i] in middle_char:
                    continue
                else:
                    middle_char.add(s[i])
                    result += 1
        
        return result