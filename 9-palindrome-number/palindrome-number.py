class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        rx=''
        for i in x:
            rx= i + rx
        if rx==x:
            return True
        else :
            return False
