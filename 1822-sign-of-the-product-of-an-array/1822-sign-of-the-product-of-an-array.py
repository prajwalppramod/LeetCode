class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product=1
        for i in range(len(nums)):
            product*=nums[i]
        def signFunc(x): 
            if x>0:
                return 1
            elif x==0:
                return 0
            else:
                return -1
        return signFunc(product)
