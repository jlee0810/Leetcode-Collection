class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) != 2:
            new_num = ""
            for i in range(1, len(s)):
                digit = (int(s[i]) + int(s[i - 1])) % 10
                new_num += str(digit)
            s = new_num
        
        return new_num[0] == new_num[1]