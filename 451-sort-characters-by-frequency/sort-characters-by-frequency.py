class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        result=''
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        d=dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        for i in d:
            result+=i*d[i]
        return result