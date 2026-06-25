class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        count=0
        for i in range(len(nums)):
            trgt=0
            for j in range(i,len(nums)):
                if nums[j]==target:
                    trgt+=1
                if trgt*2>(j-i+1):
                    count+=1
        return count