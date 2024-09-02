class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s
        
        counter = Counter(s)
        
        max_heap = []
        for char, count in counter.items():
            heapq.heappush(max_heap, (-count, char))
        
        ans = []
        cooldown = deque()
        
        while max_heap:
            count, char = heapq.heappop(max_heap)
            ans.append(char)
            
            cooldown.append((char, count + 1))

            if len(cooldown) >= k:
                front_char, front_count = cooldown.popleft()
                if -front_count > 0:
                    heappush(max_heap, (front_count, front_char))
        
        return ''.join(ans) if len(ans) == len(s) else ""
