class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        stockPrices.sort()
        
        def normalize(dx, dy):
            if dx == 0:
                return (1, 0) if dy > 0 else (-1, 0)
            if dy == 0:
                return (0, 1) if dx > 0 else (0, -1)
            g = gcd(dx, dy)
            return (dy // g, dx // g) if dx > 0 else (-dy // g, -dx // g)
        
        lines = 0
        last_slope = None
        
        for i in range(1, len(stockPrices)):
            x1, y1 = stockPrices[i - 1]
            x2, y2 = stockPrices[i]

            dx = x2 - x1
            dy = y2 - y1
            
            curr_slope = normalize(dx, dy)
            
            if curr_slope != last_slope:
                lines += 1
                last_slope = curr_slope
        
        return lines