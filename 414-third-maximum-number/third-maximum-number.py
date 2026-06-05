class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n=set(nums)
        n=list(n)
        n.sort()
        if len(n)>2:
            return n[-3]
        else:
            return max(nums)