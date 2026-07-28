class Solution:
    def reverseWords(self, s: str) -> str:

# Solving in space: O(1), using result string
               
        result = ""
        i = len(s) - 1

        # Loop string 's', character by characrter
        while i >= 0:
            #checking if character is an empty, then decrease by 1
            while i>=0 and s[i]==" ":
                i -= 1

            # Out-of-bound/ Empty
            if i < 0:
                break

            # Looping non-emppty character, till a space is found
            end = i
            while i>=0 and s[i] != " ":
                i -= 1

            word = s[i+1 : end+1]

            # Add a space, if it is not an empty string
            if result != "":
                result += " " 

            result += word

        return result


