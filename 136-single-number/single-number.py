class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d={i:nums.count(i) for i in nums}
        for i in d:
            if d[i]==1:
                return i