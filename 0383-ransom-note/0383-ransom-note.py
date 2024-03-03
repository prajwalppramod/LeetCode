
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if ransomNote == '':
            return True  # Empty ransomNote can always be constructed
        elif magazine == '':
            return False  # If magazine is empty, it's not possible to construct ransomNote
        
        for i in ransomNote:
            if i in magazine:
                magazine = magazine.replace(i, '', 1)  # Replace only one occurrence
            else:
                return False  # If any character of ransomNote is not found in magazine, return False
        return True

            