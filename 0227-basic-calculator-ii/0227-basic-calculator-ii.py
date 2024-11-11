class Solution:
    def calculate(self, s: str) -> int:
        prev_op = '+'
        num = 0 
        stck = []

        for idx, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            if not c.isdigit() and c != ' ' or idx == len(s) - 1:
                if prev_op == '+':
                    stck.append(num)
                elif prev_op == '-':
                    stck.append(-num)
                elif prev_op == '*':
                    stck.append(stck.pop() * num)
                elif prev_op == '/':
                    stck.append(int(stck.pop() / num))
                prev_op = c
                num = 0
        return sum(stck)