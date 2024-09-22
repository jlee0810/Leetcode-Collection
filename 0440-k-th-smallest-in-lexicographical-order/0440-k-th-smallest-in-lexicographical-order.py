class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_steps(current, n):
            steps = 0
            first = current
            last = current + 1
            while first <= n:
                steps += min(n + 1, last) - first
                first *= 10
                last *= 10
            return steps
        
        current = 1
        k -= 1

        while k > 0:
            steps = count_steps(current, n)
            if steps <= k:
                current += 1
                k -= steps
            else:
                current *= 10
                k -= 1
        
        return current
