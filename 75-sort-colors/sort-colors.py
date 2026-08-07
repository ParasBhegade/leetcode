class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n=len(nums)
        for i in range(n):
            mini=i
            for j in range(i+1,n):
                if nums[j]<nums[mini]:
                    mini=j
            nums[i],nums[mini]=nums[mini],nums[i]
        return nums
