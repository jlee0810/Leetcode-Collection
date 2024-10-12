class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        time = defaultdict(int)
        max_time = 0

        for start, end in intervals:
            time[start] += 1
            time[end + 1] -= 1
            max_time = max(max_time, end)

        min_groups = 0
        current_groups = 0

        for t in range(max_time + 1):
            current_groups += time[t]
            min_groups = max(min_groups, current_groups)

        return min_groups