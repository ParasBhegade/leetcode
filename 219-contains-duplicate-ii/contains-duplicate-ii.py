class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums)==len(set(nums)):
            return False
        else:
            d={}
            for i in range(len(nums)):
                if nums[i] not in d:
                    d[nums[i]]=i
                else:
                    if abs(d[nums[i]]-i)<=k:
                        return True
                    d[nums[i]]=i
            return False