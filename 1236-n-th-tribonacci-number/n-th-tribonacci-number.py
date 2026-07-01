class Solution:
    def tribonacci(self, n: int) -> int:
        mem={}
        def memo(n,mem):
            if n ==0:
                return 0
            elif n==1:
                return 1
            elif n==2:
                return 1
            elif n in mem:
                return mem[n]
            else:
                mem[n]= memo(n-1,mem) + memo(n-2,mem) + memo(n-3,mem)
            return mem[n]
        return memo(n,mem)