class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x != root_y:
                if root_x < root_y:
                    parent[root_y] = root_x
                else:
                    parent[root_x] = root_y

        parent = [i for i in range(26)]

        for c1, c2 in zip(s1, s2):
            union(ord(c1) - ord('a'), ord(c2) - ord('a'))

        result = []
        for char in baseStr:
            result.append(chr(find(ord(char) - ord('a')) + ord('a')))

        return ''.join(result)