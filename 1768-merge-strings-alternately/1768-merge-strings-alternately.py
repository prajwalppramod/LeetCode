class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_string = ""
        max_length = max(len(word1), len(word2))
        
        for i in range(max_length):
            if i < len(word1):
                merged_string += word1[i]
            if i < len(word2):
                merged_string += word2[i]
        
        return merged_string
