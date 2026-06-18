class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        m_angle = minutes * 6
        h_angle=hour_angle = (hour % 12) * 30 + minutes * 0.5
        result= abs(m_angle-h_angle)
        if result < 180:
            return result
        return (360-result)