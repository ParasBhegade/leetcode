import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumeven=n*(n+1)
        sumodd=n**2
        return math.gcd(sumodd,sumeven)