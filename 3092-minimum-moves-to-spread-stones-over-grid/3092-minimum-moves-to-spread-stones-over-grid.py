class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        start_state = tuple(sum(grid, []))
        target_state = (1, 1, 1, 1, 1, 1, 1, 1, 1)
        queue = deque([(start_state, 0)])
        
        visited = set()
        visited.add(start_state)
        
        adjacency = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4, 6],
            4: [1, 3, 5, 7],
            5: [2, 4, 8],
            6: [3, 7],
            7: [4, 6, 8],
            8: [5, 7]
        }
        
        while queue:
            current_state, moves = queue.popleft()
            
            if current_state == target_state:
                return moves
            
            for i in range(9):
                if current_state[i] > 1:
                    for neighbor in adjacency[i]:
                        new_state = list(current_state)
                        new_state[i] -= 1
                        new_state[neighbor] += 1
                        new_state_tuple = tuple(new_state)

                        if new_state_tuple not in visited:
                            visited.add(new_state_tuple)
                            queue.append((new_state_tuple, moves + 1))               
        
        return -1