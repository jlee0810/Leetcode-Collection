class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        cnt = Counter(s)

        odd = False
        for value in cnt.values():
            if value % 2 == 0:
                continue
            else:
                if odd == True:
                    return False
                odd = True
        return True