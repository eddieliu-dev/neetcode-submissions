class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights)-1
        maxVol = 0
        while start != end:
            vol = (end-start)*min(heights[start],heights[end])
            maxVol = max(maxVol,vol)
            if heights[start]<heights[end]:
                start+=1
            else:
                end-=1
        return maxVol