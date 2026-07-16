from math import gcd
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        mx=0
        prefixGcd=[]
        result=0
        for i in range(len(nums)):
            if i == 0:
                mx=nums[0]
                prefixGcd.append(nums[0])
            else:
                mx=max(mx,nums[i])
                prefixGcd.append(gcd(nums[i],mx))
        prefixGcd.sort()
        if len(prefixGcd)%2!=0:
            prefixGcd.pop(len(prefixGcd)//2)
        left=0
        right=len(prefixGcd)-1
        while left<right:
            result+=gcd(prefixGcd[left],prefixGcd[right])
            left+=1
            right-=1
        return result