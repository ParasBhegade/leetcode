class Solution:
    def minElement(self, nums: List[int]) -> int:
        num=''
        for i in range(len(nums)):
            su=0
            num=str(nums[i])
            for j in num:
                su=su+int(j)
            nums[i]=su
        return min(nums)