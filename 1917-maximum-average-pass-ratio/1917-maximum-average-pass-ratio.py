class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        max_heap = []

        for c in classes:
            p, total = c
            improvement = ((p + 1) / (total + 1)) - (p / total)
            heappush(max_heap, (-improvement, p, total))
        
        while extraStudents:
            student, p, total = heappop(max_heap)
            p += 1
            total += 1
            extraStudents -= 1

            improvement = ((p + 1) / (total + 1)) - (p / total)
            heappush(max_heap, (-improvement, p, total))
        
        pass_ratio = 0 
        student_count = len(max_heap)

        while max_heap:
            _, p, total = heappop(max_heap)
            pass_ratio += (p / total)
        
        return pass_ratio / student_count