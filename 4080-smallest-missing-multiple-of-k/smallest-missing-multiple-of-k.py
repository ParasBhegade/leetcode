class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        ss=set(nums)
        mul=k
        while mul in ss:
            mul+=k
        return mul