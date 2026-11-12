class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxw=0
        l=0 
        r=len(heights)-1
        while l<r:
            water= (r - l) * min(heights[l], heights[r])
            maxw=max(maxw,water)
            if heights[l]< heights[r]: l+=1
            else: r-=1
        return maxw

        