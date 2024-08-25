class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = deque()
        a = a[::-1]    
        b = b[::-1]
        carry = 0      
        i = 0

        while i < min(len(a), len(b)):
            curr_sum = int(a[i]) + int(b[i]) + carry
            result.appendleft(str(curr_sum % 2))
            carry = curr_sum // 2
            i += 1

        while i < len(a):
            curr_sum = int(a[i]) + carry
            result.appendleft(str(curr_sum % 2))
            carry = curr_sum // 2
            i += 1

        while i < len(b):
            curr_sum = int(b[i]) + carry
            result.appendleft(str(curr_sum % 2))
            carry = curr_sum // 2
            i += 1

        if carry:
            result.appendleft('1')

        return ''.join(result)