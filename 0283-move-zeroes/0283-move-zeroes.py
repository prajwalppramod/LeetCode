class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nextnonzero = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[nextnonzero]=nums[i];
                nextnonzero+=1
        for i in range(nextnonzero, len(nums)):
            nums[i]=0
                
        