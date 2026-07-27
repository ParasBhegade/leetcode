class Solution:
    def isPalindrome(self, x: int) -> bool:
        result=0
        num=x
        while x>0:
            result=(result*10)+(x%10)
            x=x//10
        if result==num:
            return True
        else:
            return False
