class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hsh={}
        ss=list(s.split(' '))
        if len(pattern)!=len(ss):
            return False
        else:
            for i in range(len(pattern)):
                if pattern[i] not in hsh:
                    if ss[i] in hsh.values():
                        return False
                    hsh[pattern[i]]=ss[i]
                elif hsh[pattern[i]]!=ss[i]:
                    return False
        return True