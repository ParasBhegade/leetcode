class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min=arr[1]-arr[0]
        l=[]
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]<min:
                min=arr[i+1]-arr[i]
        for i in range(len(arr)-1):
                if abs(arr[i+1]-arr[i])==min:
                    l.append([arr[i],arr[i+1]])
        return l