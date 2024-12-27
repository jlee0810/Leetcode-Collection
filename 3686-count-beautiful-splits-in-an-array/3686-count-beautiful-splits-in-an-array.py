class Solution:
    def beautifulSplits(self, nums: List[int]) -> int:
        ns = "".join((chr(48 + n) for n in nums))
        bc = 0
        for i in range(1, len(ns) - 1):
            if ns[i : 2 * i] == ns[:i]:
                bc += len(ns) - 2 * i
                for j in range(i + 1, 2 * i):
                    if ns[j : 2 * j - i] == ns[i:j]:
                        bc += 1
            else:
                for j in range(i + 1, len(ns)):
                    if ns[j : 2 * j - i] == ns[i:j]:
                        bc += 1
        return bc
