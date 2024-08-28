class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def is_palindromic(num_list):
            l, r = 0, len(num_list) - 1
            while l <= r:
                if num_list[l] != num_list[r]:
                    return False
                l += 1
                r -= 1
            return True

        for base in range(2, n - 1):
            num = []
            temp = n
            while temp > 0:
                num.append(temp % base)
                temp //= base

            if not is_palindromic(num):
                return False

        return True
