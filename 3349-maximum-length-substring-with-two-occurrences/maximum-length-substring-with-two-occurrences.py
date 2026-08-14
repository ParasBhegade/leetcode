class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        d={}
        lft=0 
        res=0
        for rgt in range(len(s)):
            d[s[rgt]]=d.get(s[rgt],0)+1
            while d[s[rgt]]>2:
                d[s[lft]]-=1
                lft+=1
            res=max(res,rgt-lft+1)
        return res