class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        length_nm = len(rolls) + n
        target = length_nm * mean
        n_sum = target - sum(rolls)

        if n_sum < n or n_sum > 6 * n:
            return []

        base = n_sum // n
        remainder = n_sum % n
        
        result = [base] * n
        
        for i in range(remainder):
            result[i] += 1

        for r in result:
            if r < 1 or r > 6:
                return []

        return result