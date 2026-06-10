class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zero=[]
        zero=[]
        for i in range(len(nums)):
            if nums[i]!=0:
                non_zero.append(nums[i])
            else:
                zero.append(nums[i])
        nums.clear()
        nums.extend(non_zero)
        nums.extend(zero)
        return nums