class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        prev_operator = '+'

        for i in range(len(s)):
            char = s[i]

            if char.isdigit():
                num = num * 10 + int(char)
            
            if not char.isdigit() and char != ' ' or i == len(s):
                if prev_operator == '+':
                    stack.append(num)
                if prev_operator == '-':
                    stack.append(-num)
                if prev_operator == '*':
                    stack.append(stack.pop() * num)
                if prev_operator == '/':
                    stack.append(int(stack.pop() / num))
                
                prev_operator = char
                num = 0
        if prev_operator == '+':
            stack.append(num)
        if prev_operator == '-':
            stack.append(-num)
        if prev_operator == '*':
            stack.append(stack.pop() * num)
        if prev_operator == '/':
            stack.append(int(stack.pop() / num))
            
        return sum(stack)