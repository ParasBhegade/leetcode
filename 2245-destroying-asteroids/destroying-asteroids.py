class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        init=mass
        asteroids.sort()
        for i in asteroids:
            if mass>=i:
                mass+=i
        if mass==sum(asteroids)+init:
            return True
        else:
            return False