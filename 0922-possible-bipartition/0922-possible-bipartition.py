class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        dislike_dict = defaultdict(list)

        for p1, p2 in dislikes:
            dislike_dict[p1].append(p2)
            dislike_dict[p2].append(p1)
        
        color = {}

        def dfs(person, current_color):
            color[person] = current_color
            
            for neighbor in dislike_dict[person]:
                if neighbor not in color:
                    if not dfs(neighbor, -current_color):
                        return False
                elif color[neighbor] == current_color:
                    return False
                
            return True

        for person in range(1, n + 1):
            if person not in color:
                if not dfs(person, 1):
                    return False

        return True
