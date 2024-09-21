class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []

        def dfs(num):
            if num > n:
                return
            result.append(num)
            for i in range(10):
                if num * 10 + i > n:
                    break
                dfs(num * 10 + i)

        for i in range(1, 10):
            dfs(i)
            
        return result
 

        # result = []
        # current = 1

        # for _ in range(n):
        #     result.append(current)

        #     if current * 10 <= n:
        #         current *= 10
        #     else:
        #         while current % 10 == 9 or current >= n:
        #             current //= 10
        #         current += 1

        # return result