class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mcount=0
        curr=0
        for i in nums:
            if i==1:
                curr+=1
            else:
                mcount=max(mcount,curr)
                curr=0
        return max(mcount,curr)