class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort(key=lambda interval: interval[0])
        slots2.sort(key=lambda interval: interval[0])

        i, j = 0, 0

        while i < len(slots1) and j < len(slots2):
            working_start = max(slots1[i][0], slots2[j][0])
            working_end = min(slots1[i][1], slots2[j][1])

            if working_end - working_start >= duration:
                return [working_start, working_start + duration]

            if slots1[i][1] > slots2[j][1]:
                j += 1
            else:
                i += 1

        return []