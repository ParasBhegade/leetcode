class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        mod=(10**9)+7
        l=[1]*len(s)
        l2=[1]*len(s)
        l3=[0]*len(s)
        ss=[]
        prefix=0
        pre=0
        num=0
        count=0
        for i in range(len(s)):
            #nonZero Count
            #concat
            if s[i]!="0":
                count+=1
                l3[i]=count
                pre=((pre*10)+int(s[i]))%mod
                l2[i]=pre
            else:
                l3[i]=count
                l2[i]=pre
            #prefix
            prefix+=int(s[i])
            l[i]=prefix
        for left,right in queries:
            if left==0:
                count=l3[right]
                num=l2[right]
            else :
                count = l3[right] - l3[left-1]
                num = (l2[right] - (l2[left-1] * pow(10, count, mod))) % mod
            if num==0:
                ss.append(0)
            else:
                if left>0:
                    ss.append((((l[right])-l[left-1])*num)%mod)
                else:
                    ss.append((l[right]*num)%mod)
            num=0
        return ss