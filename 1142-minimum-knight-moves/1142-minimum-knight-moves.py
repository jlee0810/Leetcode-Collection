class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        
        q = deque([(0, 0, 0)])
        visited = set((0, 0))
        
        while q:
            curr_x, curr_y, curr_move = q.popleft()
            
            if curr_x == x and curr_y == y:
                return curr_move
            
            for dx, dy in [[-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2]]:
                new_x, new_y = curr_x + dx, curr_y + dy
                
                if (new_x, new_y) not in visited and new_x >= -1 and new_y >= -1:
                    visited.add((new_x, new_y))
                    q.append((new_x, new_y, curr_move + 1))
        
        return -1
