class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator== 0:
            return "0"

        res = []

        # Handle sign
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")

        numerator, denominator = abs(numerator),abs(denominator)

        # Integer part
        res.append(str(numerator // denominator))
        r = numerator % denominator

        if r == 0:
            return "".join(res)

        res.append(".")
        # Map r -> position in result
        r_map = {}

        while r != 0:
            if r in r_map:
                idx = r_map[r]
                res.insert(idx, "(")
                res.append(")")
                break

            r_map[r] = len(res)
            r *= 10
            res.append(str(r // denominator))
            r %= denominator

        return "".join(res)

