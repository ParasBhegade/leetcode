class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target  in nums :
            for i in range(len(nums)):
                if nums[i]==target:
                    return i
        else:
            if target>nums[-1]:
                return len(nums)
            elif len(nums)==1:
                if target<nums[0]:
                    return 0
                else : 
                    return 1
            else:
                for i in range(len(nums)):
                    for j in range(i+1,len(nums)):
                        if target>nums[i] and target<nums[j]:
                            return j
                        elif target<nums[i] :
                            return i