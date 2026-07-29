class Solution:
    def romanToInt(self, s: str) -> int:
        guide = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100, 
            "D" : 500,
            "M" : 1000
        }

        result = 0
        for i in range(len(s)):
            if i + 1 < len(s) and guide[s[i]] < guide[s[i + 1]]:
                result -= guide[s[i]]

            else:
                result += guide[s[i]]

        return result