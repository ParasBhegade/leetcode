class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n=len(piles)
        if n==1:
            return True
        else :
            mem={}
            def solve(left,right):
                if left==right:
                    return piles[left]
                if (left,right) in mem:
                    return mem[(left,right)]
                lft=piles[left]-solve(left+1, right)
                rgt=piles[right]-solve(left,right-1)
                res=max(lft,rgt)
                mem[(left,right)]=res
                return res
        return solve(0,len(piles)-1)>=0
