class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1={}
        d2={}
        if len(s)==len(t):
            for i in s:
                if i not in d1:
                    d1[i]=1
                else:
                    d1[i]+=1
            for i in t:
                if i not in d2:
                    d2[i]=1
                else:
                    d2[i]+=1
            if d1==d2:
                return True
            else:
                return False
        else:
            return False