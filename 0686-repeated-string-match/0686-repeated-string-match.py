class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        minRepeats = math.ceil(len(b) / len(a))
        for count in range(minRepeats, minRepeats + 2):
            if b in a * count:
                return count
        return -1
        