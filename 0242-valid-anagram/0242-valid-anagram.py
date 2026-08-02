class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = [0] * 26

        # Here the only said that only lowwercase letters are present
        # So we'll set range a - z
        
        for char in s:
            freq[ord(char) - ord('a')] += 1

        for char in t:
            freq[ord(char) - ord('a')] -= 1

        for count in freq:
            if count != 0:
                return False
        
        return True
