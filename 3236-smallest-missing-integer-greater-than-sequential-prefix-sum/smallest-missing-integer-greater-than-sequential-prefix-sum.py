class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n=len(nums)
        total=0
        for i in range(n):
            if i<(n-1) and nums[i+1]==nums[i]+1:
                total+=nums[i]
            else:
                total+=nums[i]
                break
        while total in nums:
            total+=1
        return total