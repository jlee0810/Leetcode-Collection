class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        diff = cnt = 0

        for i, c in enumerate(num):
            if i < n // 2:
                if c == '?':
                    cnt += 1
                else:
                    diff += int(c)
            else:
                if c == '?':
                    cnt -= 1
                else:
                    diff -= int(c)
        
        # if diff > 0 and cnt > 0:
        #     return True
        
        diff = abs(diff)
        cnt = abs(cnt)

        return cnt * 9/ 2 != diff