class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        d={}
        lft=0 
        res=0
        for rgt in range(len(nums)):
            d[nums[rgt]]=d.get(nums[rgt],0)+1
            while d[nums[rgt]]>k:
                d[nums[lft]]-=1
                lft+=1
            res=max(res,rgt-lft+1)
        return res