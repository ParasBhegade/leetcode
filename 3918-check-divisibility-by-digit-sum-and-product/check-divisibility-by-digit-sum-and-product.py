class Solution:
    def checkDivisibility(self, n: int) -> bool:
        num=n
        add=0
        prod=1
        while num>0:
            prod*=num%10
            add+=num%10
            num//=10
        return  n%(add+prod)==0