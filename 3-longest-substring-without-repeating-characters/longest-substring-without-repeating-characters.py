class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l_sub=sub=''
        for i in s:
            if i not in sub:
                sub+=i
                if len(sub)>len(l_sub):
                    l_sub=sub
            else:
                sub= sub[sub.index(i)+1:]
                sub+=i
                if len(sub)>len(l_sub):
                    l_sub=sub
        return len(l_sub)


