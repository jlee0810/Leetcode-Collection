class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.rad = radius
        self.xc = x_center
        self.yc = y_center

    def randPoint(self) -> List[float]:
        x0 = self.xc - self.rad
        y0 = self.yc - self.rad

        while True:
            xg = x0 + random.uniform(0, 1) * 2 * self.rad
            yg = y0 + random.uniform(0, 1) * 2 * self.rad
            if math.sqrt((xg - self.xc) ** 2 + (yg - self.yc) ** 2) <= self.rad:
                return [xg, yg]



# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()