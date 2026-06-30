class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count=0
        left=a=b=c=0
        for i in range(len(s)):
            if s[i]=="a":
                    a+=1
            if s[i]=="b":
                    b+=1
            if s[i]=="c":
                    c+=1
            while a>0 and b>0 and c> 0:
                count+=len(s)-i
                if s[left] == "a":
                    a -= 1
                elif s[left] == "b":
                    b -= 1
                else:
                    c -= 1
                left += 1           
        return count