class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        stockPrices.sort()

        def slope(x1, y1, x2, y2):
            dx, dy = x2 - x1, y2- y1
            g = gcd(dx, dy)
            return (dy // g, dx // g) if dx > 0 else (-dy // g, -dx // g)

        lines = 0

        last_slope = float('inf')
        for i in range(1, len(stockPrices)):
            x1, y1 = stockPrices[i - 1]
            x2, y2 = stockPrices[i]

            curr_slope = slope(x1, y1, x2, y2)

            if curr_slope == last_slope:
                continue
            else:
                lines += 1
                last_slope = curr_slope
        
        return lines