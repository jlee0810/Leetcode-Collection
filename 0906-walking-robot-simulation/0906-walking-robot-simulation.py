class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacle_set = set()
        for obstacle in obstacles:
            obstacle_set.add((obstacle[0], obstacle[1]))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        x, y = 0, 0
        max_distance_squared = 0
        current_direction = 0

        for command in commands:
            if command == -1:
                current_direction = (current_direction + 1) % 4
                continue

            if command == -2:
                current_direction = (current_direction + 3) % 4
                continue

            dx, dy = directions[current_direction]
            for _ in range(command):
                next_x, next_y = x + dx, y + dy
                if (next_x, next_y) in obstacle_set:
                    break
                x, y = next_x, next_y

            max_distance_squared = max(max_distance_squared, x * x + y * y)

        return max_distance_squared