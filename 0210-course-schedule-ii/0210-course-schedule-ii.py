class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(set)
        indegree = [0 for _ in range(numCourses)]

        for course, pre_req in prerequisites:
            adj_list[pre_req].add(course)
            indegree[course] += 1
        
        result = []

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                result.append(i)

        while q:
            curr_course = q.popleft()
            for course in adj_list[curr_course]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)
                    result.append(course)


        return result if len(result) == numCourses else []


        