class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        d = {}
        for index, num in enumerate(sorted_nums):
            if num not in d:
                d[num] = index
        l = []
        for i in nums:
            l.append(d[i])
        return l
            