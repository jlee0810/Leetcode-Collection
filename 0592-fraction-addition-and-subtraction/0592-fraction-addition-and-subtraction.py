class Solution:
    def fractionAddition(self, expression: str) -> str:
        num = 0
        denom = 1
        idx = 0

        while idx < len(expression):
            curr_num = 0
            curr_denom = 0

            is_neg = False

            if expression[idx] == "-" or expression[idx] == "+":
                if expression[idx] == "-":
                    is_neg = True
                idx += 1

            while idx < len(expression) and expression[idx].isdigit():
                curr_num = curr_num * 10 + int(expression[idx])
                idx += 1

            if is_neg:
                curr_num *= -1

            idx += 1

            while idx < len(expression) and expression[idx].isdigit():
                curr_denom = curr_denom * 10 + int(expression[idx])
                idx += 1

            num = num * curr_denom + curr_num * denom
            denom = denom * curr_denom

            if num == 0:
                denom = 1
            else:
                gcd = self._find_gcd(abs(num), denom)
                num //= gcd
                denom //= gcd

        return f"{num}/{denom}"

    def _find_gcd(self, a, b):
        while b:
            a, b = b, a % b
        
        return a


        # min_num = min(a, b)
        # for i in range(min_num, 0, -1):
        #     if a % i == 0 and b % i == 0:
        #         return i
        # return 1
