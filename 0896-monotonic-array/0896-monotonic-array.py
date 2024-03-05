class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        incrarr = sorted(nums)
        decrarr = sorted(nums, reverse=True)
        if incrarr==nums or decrarr==nums:
            return True
        else:
            return False
            