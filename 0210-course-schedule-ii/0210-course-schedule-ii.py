class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        pre_req_count = [0 for _ in range(numCourses)]
        adj_list = defaultdict(list)

        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            pre_req_count[course] += 1

        q = deque()

        for idx, count in enumerate(pre_req_count):
            if count == 0:
                q.append(idx)
        
        while q:
            course = q.popleft()
            result.append(course)
            
            for dependent in adj_list[course]:
                pre_req_count[dependent] -= 1
                if pre_req_count[dependent] == 0:
                    q.append(dependent)

        return result if sum(pre_req_count) == 0 else []