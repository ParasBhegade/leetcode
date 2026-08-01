class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        mem={}
        def solve(left, right):
            if (left, right) in mem:
                return mem[(left,right)]
            if left==right:
                mem[(left, right)] = nums[left]
                return nums[left]
            lft=nums[left]-solve(left+1,right)
            rgt=nums[right]-solve(left,right-1)
            res=max(lft,rgt)
            mem[(left,right)]=res
            return res
        result= solve(0,len(nums)-1)
        return result >=0