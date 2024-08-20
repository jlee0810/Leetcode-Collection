class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        dislike_dict = defaultdict(list)

        for p1, p2 in dislikes:
            dislike_dict[p1].append(p2)
            dislike_dict[p2].append(p1)
        
        max_heap = []
        for key, value in dislike_dict.items():
            heapq.heappush(max_heap, (-len(value), key))

        color = {}

        while max_heap:
            _, person = heapq.heappop(max_heap)

            if person not in color:
                color[person] = 1
                stack = [person]
                
                while stack:
                    current = stack.pop()
                    current_color = color[current]
                    
                    for neighbor in dislike_dict[current]:
                        if neighbor not in color:
                            color[neighbor] = -current_color
                            stack.append(neighbor)
                        elif color[neighbor] == current_color:
                            return False

        return True
