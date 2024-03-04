class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack)<len(needle):
            return -1
        elif not needle:
            return -1
        else:
            nlen = len(needle)
            for i in range(len(haystack)):
                if haystack[i:i+len(needle)]==needle:
                    return i
        return -1
            