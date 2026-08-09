class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n=len(piles)
        suff=[0]*(n+1)
        for i in range(n-1,-1,-1):
            suff[i]=suff[i+1]+piles[i]
        mem={}
        def solve(i,M):
            if 2*M>=(n-i):
                return suff[i]
            if (i,M) in mem:
                return mem[(i,M)]
            res=suff[i]
            best=0
            for j in range(1,min(2*M,n-i)+1):
                opp=solve(i+j,max(M,j))
                curr=res-opp
                best=max(best,curr)
            mem[(i,M)]=best
            return best
        return solve(0,1)