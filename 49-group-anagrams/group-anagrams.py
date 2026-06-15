class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in range(len(strs)):
            v=''
            for j in sorted(strs[i]):
                v+=j
            if v not in d:
                d[v]=[strs[i]]
            else:
                d[v].append(strs[i])
        return list(d.values())