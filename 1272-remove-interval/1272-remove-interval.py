class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        result = []
        start, end = toBeRemoved

        for interval in intervals:
            #Doesnt overlap at all with interval being removed
            if interval[1] <= start or interval[0] >= end:
                result.append(interval)
            else:
            #There is overlap with removal and existing interval
                if interval[0] < start:
                    result.append([interval[0], start])
                if interval[1] > end:
                    result.append([end, interval[1]])

        return result
