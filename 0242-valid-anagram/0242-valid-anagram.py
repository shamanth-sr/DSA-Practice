class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S = sorted(s)
        T = sorted(t)

        return True if T == S else False