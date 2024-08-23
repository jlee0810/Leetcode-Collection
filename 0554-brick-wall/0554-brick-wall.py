class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edge_count = {}
        max_edges = 0

        for row in wall:
            edge_index = 0
            for brick_idx in range(len(row) - 1):
                edge_index += row[brick_idx]
                if edge_index in edge_count:
                    edge_count[edge_index] += 1
                else:
                    edge_count[edge_index] = 1
                max_edges = max(max_edges, edge_count[edge_index])
        
        return len(wall) - max_edges