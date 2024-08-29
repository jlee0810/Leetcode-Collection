class Solution:
    def judgeCircle(self, moves: str) -> bool:
        drow, dcol = 0, 0

        for c in moves:
            if c == 'U':
                drow += 1
            if c == 'D':
                drow -= 1
            if c == 'L':
                dcol -= 1
            if c == 'R':
                dcol += 1
            
        return drow == 0 and dcol == 0