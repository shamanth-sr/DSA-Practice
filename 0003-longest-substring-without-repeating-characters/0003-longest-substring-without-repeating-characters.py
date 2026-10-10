class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        i = 0

        ans = 0

        for j in range(len(s)):

            while s[j] in charSet:
                charSet.remove(s[i])
                i += 1

            charSet.add(s[j])
            ans = max(ans, j - i + 1)

        return ans
            
