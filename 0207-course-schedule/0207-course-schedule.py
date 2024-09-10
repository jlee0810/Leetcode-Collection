class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_req_list = defaultdict(list)
        in_degree = [0 for _ in range(numCourses)]

        for course, pre_req in prerequisites:
            pre_req_list[pre_req].append(course)
            in_degree[course] += 1
        
        q = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
        
        took = 0

        while q:
            course = q.popleft()
            took += 1
            for dependent in pre_req_list[course]:
                in_degree[dependent] -= 1
                if in_degree[dependent] == 0:
                    q.append(dependent)
                
        
        return took == numCourses