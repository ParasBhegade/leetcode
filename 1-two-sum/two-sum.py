class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         Ans= {}
         for i in range(len(nums)):
            sol = target - nums[i]
            if sol in Ans:
                return [Ans[sol], i]
            Ans[nums[i]] = i