
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # 1. Greedy check: count total hours needed at the given eating speed
        def is_feasible(speed: int) -> bool:
            hours_needed = 0
            for pile in piles:
                hours_needed += math.ceil(pile / speed)
            return hours_needed <= h

        # 2. Define search bounds: slowest (1/hr) to fastest useful speed (max pile)
        low = 1
        high = max(piles)
        res = high

        # 3. Binary search to find the minimum valid eating speed
        while low <= high:
            mid = (low + high) // 2

            if is_feasible(mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1

        return res