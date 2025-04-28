class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.height = height
        self.width = width
        self.food = food
        self.positions = deque()
        self.positions.append([0, 0])
        self.score = 0

    def move(self, direction: str) -> int:
        head = self.positions[0]

        if direction == "U":
            new_head = [head[0] - 1, head[1]]
        elif direction == "D":
            new_head = [head[0] + 1, head[1]]
        elif direction == "L":
            new_head = [head[0], head[1] - 1]
        else:
            new_head = [head[0], head[1] + 1]

        if self.positions and new_head in self.positions:
            if self.positions[-1] != new_head:
                return -1

        if (
            new_head[0] == -1
            or new_head[0] == self.height
            or new_head[1] == -1
            or new_head[1] == self.width
        ):
            return -1

        self.positions.appendleft(new_head)
        if self.food and new_head == self.food[0]:
            self.food.pop(0)
            self.score += 1
        else:
            self.positions.pop()

        return self.score


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
