from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        fractions = []
        num = ""
        if expression[0] != '-':
            expression = '+' + expression

        for i, c in enumerate(expression):
            if c in ['+', '-']:
                if num:
                    fractions.append(Fraction(num))
                num = c
            else:
                num += c
        fractions.append(Fraction(num))
        
        result = sum(fractions)
        
        return f"{result.numerator}/{result.denominator}"