class Solution:
    def myAtoi(self, s: str) -> int:
        # Null string
        if not s:
            return 0
        
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        i = 0
        n = len(s)

        # Whitespace condition
        while i < n and s[i] == ' ':
            i += 1
        if i == n:
            return 0

        # Sign condition
        sign = 1
        if s[i] == "+":
            i += 1
        elif s[i] == "-":
            sign = -1
            i += 1

        # Numeric or Non-numeric
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            result = result * 10 + digit

            if sign * result <= INT_MIN:
                return INT_MIN
            if sign * result >= INT_MAX:
                return INT_MAX

            i += 1

        return sign * result



