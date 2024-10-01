class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt = Counter(s)

        max_heap = []
        for key, val in cnt.items():
            heappush(max_heap, (-val, key))
        
        result = ""
        last = None

        while max_heap:
            count, c = heappop(max_heap)
            result += c

            if last:
                heappush(max_heap, last)
                last = None

            count += 1
            if count < 0:
                last = (count, c)

        return result if len(result) == len(s) else ""
