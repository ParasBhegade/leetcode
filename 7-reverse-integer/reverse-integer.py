class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        if x<0:
            rev=int("-"+str(abs(x))[::-1])
        else:
            rev=int(str(x)[::-1])
        if rev > ((2**31) - 1) or rev < -(2**31):
            return 0
        return rev