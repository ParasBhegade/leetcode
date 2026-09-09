class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st=set(nums)
        target=0
        for i in st:
            if i-1 not in st:
                current=1
                num=i
                while num+1 in st:
                    current+=1
                    num+=1
                target=max(current,target)
        return target