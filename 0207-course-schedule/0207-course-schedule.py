class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_list = defaultdict(list)
        in_degree = [0] * numCourses
        
        for course, pre_req in prerequisites:
            prereq_list[pre_req].append(course)
            in_degree[course] += 1
        
        q = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        processed_courses = 0
        
        while q:
            course = q.popleft()
            processed_courses += 1
            
            for dependent in prereq_list[course]:
                in_degree[dependent] -= 1
                if in_degree[dependent] == 0:
                    q.append(dependent)
        
        return processed_courses == numCourses