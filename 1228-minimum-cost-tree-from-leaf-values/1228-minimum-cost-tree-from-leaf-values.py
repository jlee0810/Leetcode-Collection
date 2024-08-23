class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        result = 0
        while len(arr) > 1:
            i = arr.index(min(arr))
            result += min(arr[i - 1 : i] + arr[i + 1 : i + 2]) * arr.pop(i)
        return result