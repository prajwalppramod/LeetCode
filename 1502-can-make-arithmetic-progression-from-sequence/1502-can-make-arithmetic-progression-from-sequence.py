class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        flag=False
        diff = arr[1]-arr[0]
        for i in range(1,len(arr)):
            if arr[i] - arr[i-1]==diff:
                flag=True
            else:
                flag=False
                break
        return flag