class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        s = set()

        curr_num = 1

        while n > 0:
            if k - curr_num not in s:
                s.add(curr_num)
                n -= 1
            curr_num += 1


        return sum(s)