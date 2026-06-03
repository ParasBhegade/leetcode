class Solution:
    def mirrorDistance(self, n: int) -> int:
        mir=int(str(n)[::-1])
        return abs(n-mir)