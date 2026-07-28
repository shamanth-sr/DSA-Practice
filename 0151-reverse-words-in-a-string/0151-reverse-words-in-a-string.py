class Solution:
    def reverseWords(self, s: str) -> str:
        # Initialise a list to store the word
        words = []

        word = ""

        # Loop through each character in the string's'
        for ch in s:
            # If we don't have a space b/w
            if ch != " ":
                word += ch
            # If we found a space
            elif word:
                words.append(word)
                word = ""

        # Last word
        if word:
            words.append(word)

        words.reverse()

        return " ".join(words)