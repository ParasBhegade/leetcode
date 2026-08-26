class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left=0
        one=0
        ans=""
        for i in range(len(s)):
            if s[i]=='1':
                one+=1

            while one>k:
                if s[left]=='1':
                    one-=1
                left+=1
            if one==k:
                while s[left]=='0':
                    left+=1
                current=s[left:i+1]
                if ans == "" or len(current) < len(ans) or (len(current) == len(ans) and current < ans):
                    ans=current
        return ans