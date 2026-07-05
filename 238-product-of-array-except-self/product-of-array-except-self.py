class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[1]*len(nums)
        prefix=1
        for i in range(len(nums)):
            left[i]=prefix
            prefix*=nums[i]
        suffix=1
        for i in range(len(nums)-1,-1,-1):
            left[i]*=suffix
            suffix*=nums[i]
        return left