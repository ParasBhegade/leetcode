class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        s1=""
        if len(strs[0])==0 or len(strs[-1])==0:
            return s1 
        elif len(strs[0]) >= len(strs[-1]):
            l=len(strs[-1])
        else: 
            l=len(strs[0])
        for i in range(l):
            if strs[0][i]==strs[-1][i]:
                s1 = s1+strs[0][i]
            else:
                break
        return s1