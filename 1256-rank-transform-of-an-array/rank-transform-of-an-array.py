class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if len(arr)==0:
            return arr
        else:
            d={}
            temp=sorted(set(arr))
            for index,i in enumerate(temp):
                    d[i]=index+1
        return [d[num] for num in arr]