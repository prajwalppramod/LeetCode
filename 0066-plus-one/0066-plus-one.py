class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        num=0
        for i in range(length):
            num+= digits[i]*(10**(length-i-1))
        num+=1
        number_str=str(num)
        digits_list = [int(char) for char in number_str]
        return digits_list