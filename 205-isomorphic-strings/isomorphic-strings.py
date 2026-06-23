class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else :
            d1={}
            d2={}
            for i in range(len(s)):
                if s[i] not in d1:
                    d1[s[i]]=t[i]
                else:
                    if d1[s[i]]!=t[i]:
                        return False
            for i in range(len(t)):
                if t[i] not in d2:
                    d2[t[i]]=s[i]
                else:
                    if d2[t[i]]!=s[i]:
                        return False
        return True