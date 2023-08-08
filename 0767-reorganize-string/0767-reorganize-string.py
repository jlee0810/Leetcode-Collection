class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = []
        for key in count:
            heappush(maxHeap, (-1 * count[key], key))


        prevChar, prevCount = '', 0
        result = ''
        while maxHeap:
            count, char = heappop(maxHeap)
            if prevCount < 0:
                heappush(maxHeap, (prevCount, prevChar))
            result += char
            prevChar, prevCount = char, count + 1

        if prevCount < 0:
            return ""
        return result