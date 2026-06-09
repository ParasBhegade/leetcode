class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        result=[]
        leftsum=rightsum=0
        Left=[]
        right=[]
        if len(nums)==1:
            result.append(0)
            return result
        for i in range(len(nums)-1):
            if i ==0:
                Left.append(0)
                right.append(0)
        for i in range(len(nums)-1):
                leftsum+=nums[i]
                Left.append(leftsum)
        for i in nums[::-1]:
                rightsum+=i
                right.append(rightsum)
        right=right[::-1]
        right.pop(0)
        for i in range(len(nums)):
            result.append(abs(Left[i]-right[i]))
        return result