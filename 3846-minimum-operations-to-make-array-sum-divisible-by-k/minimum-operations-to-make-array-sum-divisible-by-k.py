class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ss=sum(nums)
        nearest_num=(ss//k)*k
        return ss-nearest_num