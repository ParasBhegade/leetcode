class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor=0
        arr=[0]*len(nums)
        if arr==nums:
            return 0
        for i in nums:
            xor^=i
        if xor==0:
            return len(nums)-1
        else:
            return len(nums)