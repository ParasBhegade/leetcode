class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        if arr!=sorted(arr):
            arr.sort()
        if arr[0]!=1:
            arr[0]=1
        for i in range(len(arr)-1):
            if not abs(arr[i]-arr[i+1])<=1:
                arr[i+1]=arr[i]+1
        return max(arr)