class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        max_time = -1
        for perm in permutations(arr):
            h1, h2, m1, m2 = perm
            hour = h1 * 10 + h2
            minute = m1 * 10 + m2
            if hour < 24 and minute < 60:
                max_time = max(max_time, hour * 60 + minute)
        
        if max_time == -1:
            return ""
        else:
            return "{:02}:{:02}".format(max_time // 60, max_time % 60)