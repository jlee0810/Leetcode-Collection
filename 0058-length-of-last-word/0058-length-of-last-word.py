class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_list = list(s.split(" "))
        filtered = []
        for word in s_list:
            if len(word) >= 1:
                filtered.append(word)
        return len(filtered[-1])
