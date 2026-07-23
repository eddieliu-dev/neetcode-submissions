class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = 0

        while l <= r:
            m = l + (r - l) // 2
            time = 0
            for p in piles:
                time += (p + m - 1) // m
            if time <= h:
                k = m
                r = m - 1
            else:
                l = m + 1
        return k
        