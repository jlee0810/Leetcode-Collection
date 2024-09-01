class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != (m * n):
            return []

        result = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(len(result)):
            for j in range(len(result[0])):
                result[i][j] = original[i * n + j]

        return result