class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d={}
        for i in text:
            if i in "balon":
                if i not in d:
                    d[i]=1
                else:
                    d[i]+=1
        for i in "balon":
            if i not in d:
                return 0
        d['l']=d['l']//2
        d['o']=d['o']//2
        return min(list(d.values()))