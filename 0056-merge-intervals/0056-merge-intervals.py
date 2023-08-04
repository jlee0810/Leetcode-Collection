class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            prevInterval = result[-1]
            currInterval = intervals[i]

            if prevInterval[1] >= currInterval[0]:
                result[-1] = [min(prevInterval[0], currInterval[0]), max(prevInterval[1], currInterval[1])]
            else:
                result.append(currInterval)

        return result
