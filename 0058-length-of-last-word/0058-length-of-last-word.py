class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = len(s)
        lastWordLength = 0
        i = length - 1
        
        # Skip trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1
        
        # Count characters of last word
        while i >= 0 and s[i] != ' ':
            lastWordLength += 1
            i -= 1
        
        return lastWordLength