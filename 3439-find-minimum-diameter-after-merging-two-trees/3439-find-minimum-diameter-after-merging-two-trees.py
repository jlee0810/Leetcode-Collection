class Solution:
    def minimumDiameterAfterMerge(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> int:
        adj_1 = defaultdict(list)
        adj_2 = defaultdict(list)

        for n1, n2 in edges1:
            adj_1[n1].append(n2)
            adj_1[n2].append(n1)

        for u1, u2 in edges2:
            adj_2[u1].append(u2)
            adj_2[u2].append(u1)

        diameter1 = self.diameter(adj_1)
        diameter2 = self.diameter(adj_2)

        half_d1 = (diameter1 + 1) // 2
        half_d2 = (diameter2 + 1) // 2

        new_diameter_candidate = half_d1 + half_d2 + 1

        min_possible_diameter = max(diameter1, diameter2, new_diameter_candidate)

        return min_possible_diameter

    def diameter(self, adj_list: defaultdict) -> int:
        if not adj_list:
            return 0

        arbitrary_node = next(iter(adj_list))
        far_node, _ = self.bfs_farthest(arbitrary_node, adj_list)

        # Perform BFS from the farthest node found to determine the diameter
        _, diameter = self.bfs_farthest(far_node, adj_list)

        return diameter

    def bfs_farthest(self, start: int, adj_list: defaultdict) -> (int, int):
        visited = set()
        queue = deque([(start, 0)])
        visited.add(start)

        farthest_node = start
        max_distance = 0

        while queue:
            current_node, distance = queue.popleft()

            if distance > max_distance:
                max_distance = distance
                farthest_node = current_node

            for neighbor in adj_list[current_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1))

        return farthest_node, max_distance
