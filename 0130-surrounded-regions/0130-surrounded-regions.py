class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited = set()
            visited.add((r, c))

            while q:
                curr_r, curr_c = q.popleft()
                board[curr_r][curr_c] = "T"
                for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    new_r, new_c = curr_r + dr, curr_c + dc
                    if (
                        0 <= new_r < len(board)
                        and 0 <= new_c < len(board[0])
                        and (new_r, new_c) not in visited
                        and board[new_r][new_c] == "O"
                    ):
                        q.append((new_r, new_c))
                        visited.add((new_r, new_c))

        for i in range(len(board)):
            if board[i][0] == "O":
                bfs(i, 0)
            if board[i][len(board[0]) - 1] == "O":
                bfs(i, len(board[0]) - 1)

        for i in range(len(board[0])):
            if board[0][i] == "O":
                bfs(0, i)
            if board[len(board) - 1][i] == "O":
                bfs(len(board) - 1, i)

                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "T":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
