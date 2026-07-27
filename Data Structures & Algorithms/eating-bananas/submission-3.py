class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        k = end

        while start <= end:
            time = 0
            m = start + (end - start) // 2
            for p in piles:
                time += (p + m - 1) // m
            if time <= h:
                k = m
                end = m - 1
            else:
                start = m + 1
        return k
        