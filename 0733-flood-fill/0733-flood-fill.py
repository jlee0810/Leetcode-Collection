class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROW, COL = len(image), len(image[0])

        startingColor = image[sr][sc]

        visited = set()
        
        def dfs(r, c):
            if r < 0 or c < 0 or r == ROW or c == COL or image[r][c] != startingColor or (r, c) in visited:
                return
            image[r][c] = color
            visited.add((r,c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image