class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=[i for i in range(len(nums)+1)]
        for i in n:
            if i not in nums:
                return i