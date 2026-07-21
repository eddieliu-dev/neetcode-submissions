class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxV = 0
        vol = 0
        for i in range(len(heights)-1):
            for j in range(i+1, len(heights)):
                width = j-i
                height = min(heights[i],heights[j])
                vol = height*width
                maxV = max(maxV, vol)
        return maxV