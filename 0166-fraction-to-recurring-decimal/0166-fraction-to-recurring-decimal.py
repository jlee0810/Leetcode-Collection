class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        isNeg = (numerator < 0) ^ (denominator < 0)

        numerator, denominator = abs(numerator), abs(denominator)

        divided = numerator // denominator
        remainder = numerator % denominator

        result = []

        if isNeg:
            result.append("-")

        result.append(str(divided))

        if remainder == 0:
            return "".join(result)

        result.append(".")

        lookup = {}
        lookup[remainder] = len(result)

        while remainder != 0:
            numerator = remainder * 10

            divided = numerator // denominator
            remainder = numerator % denominator

            if remainder in lookup:
                result.insert(lookup[remainder], "(")
                result.append(str(divided))
                result.append(")")
                return "".join(result)

            result.append(str(divided))
            lookup[remainder] = len(result)

        return "".join(result)
