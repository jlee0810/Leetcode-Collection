class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a = b = c = 0

        for x, y, z in triplets:
            if x <= target[0] and y <= target[1] and z <= target[2]:
                a = max(a, x)
                b = max(b, y)
                c = max(c, z)
        return [a, b, c] == target