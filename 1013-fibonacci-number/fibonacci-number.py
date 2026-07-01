class Solution:
    def fib(self,n):
        mem={}
        def memo(n,mem):
            if n ==0:
                return 0
            elif n==1:
                return 1
            elif n in mem:
                return mem[n]
            else:
                mem[n]= memo(n-1,mem) + memo(n-2,mem)
            return mem[n]
        return memo(n,mem)
        