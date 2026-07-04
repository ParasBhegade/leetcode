class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == 0 :
            return []
        d={}
        result=[]
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        d=sorted(d.items(), key=lambda x: x[1], reverse=True)
        for i in d[:k]:
            result.append(i[0])
        return result