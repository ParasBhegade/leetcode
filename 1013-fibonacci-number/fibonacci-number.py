class Solution:
    def fib(self, n: int) -> int:
        mem={}
        if n ==0:
            return 0
        elif n==1:
            return 1
        else:
            if n in mem:
                return mem[n]
            else:
                mem[n]= self.fib(n-1) + self.fib(n-2)
        return mem[n]