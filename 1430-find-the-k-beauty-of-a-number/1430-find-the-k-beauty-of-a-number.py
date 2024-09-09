class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        beauty = 0
        l = 0
        for r in range(k, len(str(num)) + 1):
            sub_str = str(num)[l:r]
            l += 1
            if int(sub_str) == 0:
                continue
            if num % int(sub_str) == 0:
                beauty += 1

        return beauty