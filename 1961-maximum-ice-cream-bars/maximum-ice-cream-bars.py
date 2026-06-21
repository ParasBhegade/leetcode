class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        s=sorted(costs)
        count=0
        if coins > sum(costs):
            return len(costs)
        else:
            for i in range(len(s)):
                if s[i]<=coins:
                    count+=1
                    coins-=s[i]
        return count