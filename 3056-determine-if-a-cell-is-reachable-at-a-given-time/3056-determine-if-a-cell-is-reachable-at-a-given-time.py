class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        x_dist = abs(fx - sx)
        y_dist = abs(fy - sy)
        
        if t < x_dist or t < y_dist:
            return False
        
        if x_dist == 0 and y_dist == 0 and t == 1:
            return False
            
        return True