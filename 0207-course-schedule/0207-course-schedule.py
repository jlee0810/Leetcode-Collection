class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_req = defaultdict(set)
        post_req = defaultdict(set)
        
        for course, pre in prerequisites:
            pre_req[course].add(pre)
            post_req[pre].add(course)
    
        q = deque([i for i in range(numCourses) if not pre_req[i]])
        took = set()
    
        while q:
            can_take = q.popleft()
            took.add(can_take)
            
            for course in post_req[can_take]:
                pre_req[course].remove(can_take)
                if len(pre_req[course]) == 0:
                    q.append(course)
    
        return len(took) == numCourses
