class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        adj_list = defaultdict(list)
        restricted = set(restricted)
        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        q = deque()
        q.append(0)
        visited = set()
        visited.add(0)

        while q:
            curr_node = q.popleft()
            for possible_node in adj_list[curr_node]:
                if possible_node not in visited and possible_node not in restricted:
                    q.append(possible_node)
                    visited.add(possible_node)

        return len(visited)