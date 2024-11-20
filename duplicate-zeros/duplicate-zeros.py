class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        arr1 = []
        count = 0 
        while count<len(arr):
            for i in arr:
                if i==0:
                    arr1.append(i)
                    arr1.append(i)
                    count+=2
                else:
                    arr1.append(i)
                    count+=1
        for i in range(len(arr)):
            arr[i] = arr1[i]
        