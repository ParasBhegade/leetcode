class Solution:
    def check(self, nums: List[int]) -> bool:
        Break =0
        n2=sorted(nums)
        if nums == n2:
            return True
        for i in range(len(nums)-1):
                if nums[i]>nums[i+1]:
                    Break +=1
        if nums[-1]>nums[0]:
            Break+=1
        if Break ==1:
            return True
        elif Break >2 :
            return False
        return False