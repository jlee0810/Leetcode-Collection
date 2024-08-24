class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        candidates = set()

        candidates.add(str(10 ** (length - 1) - 1))
        candidates.add(str(10 ** length + 1))

        prefix = int(n[:(length + 1) // 2])

        for i in [-1, 0, 1]:
            new_prefix = str(prefix + i)
            if length % 2 == 0:
                palindrome = new_prefix + new_prefix[::-1]
            else:
                palindrome = new_prefix + new_prefix[:-1][::-1]
            candidates.add(palindrome)

        candidates.discard(n)

        def closest_palindrome(x):
            return abs(int(x) - int(n)), int(x)

        return min(candidates, key=closest_palindrome)
