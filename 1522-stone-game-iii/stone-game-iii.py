from functools import cache
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n=len(stoneValue)
        @cache
        def solve(i):
            if i>=n:
                return 0
            take=0
            best=None
            for j in range(3):
                if i+j>=n:
                    break
                take+=stoneValue[i+j]
                adv= take - solve(i+j+1)
                if best is None or adv>best:
                    best=adv
            return best
        diff=solve(0)
        if diff>0:
            return "Alice"
        elif diff<0:
            return "Bob"
        else:
            return "Tie"
