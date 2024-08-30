class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        def bfs(r, c):
            q = deque()
            q.append((r, c, 0))
            visited = set()
            visited.add((r, c))

            while q:
                curr_r, curr_c, curr_dist = q.popleft()
                for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    nr, nc = curr_r + dr, curr_c + dc
                    if 0 <= nr < len(rooms) and 0 <= nc < len(rooms[0]) and (nr, nc) not in visited and rooms[nr][nc] != -1 and rooms[nr][nc] != 0:
                        q.append((nr, nc, curr_dist + 1))
                        visited.add((nr, nc))
                        rooms[nr][nc] = min(rooms[nr][nc], curr_dist + 1)

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    bfs(i, j)