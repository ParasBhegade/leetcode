class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k>len(nums):
            k=k%len(nums)
        l1=nums[-k:]+nums[:-k] 
        for i in range(len(nums)):
            nums[i]=l1[i]
