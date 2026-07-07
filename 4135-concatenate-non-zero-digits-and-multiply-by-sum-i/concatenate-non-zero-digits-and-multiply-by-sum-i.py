class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x=''
        s=0
        if n==0:
            return 0
        else:
            while n>0:
                if n%10!=0:
                    digit=n%10
                    s+=digit
                    x=str(digit)+x
                n//=10
        return int(x)*s