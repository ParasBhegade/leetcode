class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s=set(nums)
        s=list(s)
        if sorted(s)==sorted(nums):
            return False
        else:
            return True