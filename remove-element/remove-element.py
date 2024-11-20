class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)  # Remove the element and stay on the same index
            else:
                i += 1  # Move to the next index only if no removal occurs
        return len(nums)