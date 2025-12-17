class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        sign = 1
        result = 0

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        # 1. Ignore leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # 2. Handle optional sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        # 3. Convert digits
        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')

            # 4. Handle overflow before it happens
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            i += 1

        return sign * result
