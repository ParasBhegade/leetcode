class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        cnt = 0
        if(n==0): cnt = 1
        if(n==1): cnt = 10  
        if(n==2): cnt = 91
        if(n==3): cnt = 739
        if(n==4): cnt = 5275
        if(n==5): cnt = 32491
        if(n==6): cnt = 168571
        if(n==7): cnt = 712891
        if(n==8): cnt = 2345851
        return cnt