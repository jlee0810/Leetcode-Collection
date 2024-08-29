class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        in_nodes = [0 for _ in range(numCourses)]

        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            in_nodes[course] += 1

        ordering = []
        took = set()

        q = deque()
        for i in range(numCourses):
            if in_nodes[i] == 0:
                q.append(i)
        
        while q:
            curr_course = q.popleft()
            ordering.append(curr_course)
            took.add(curr_course)
            for course in adj_list[curr_course]:
                if course in took:
                    continue
                in_nodes[course] -= 1
                if in_nodes[course] == 0:
                    q.append(course)
        
        for required in in_nodes:
            if required > 0:
                return []
        
        return ordering