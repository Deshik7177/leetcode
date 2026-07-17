class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        area=0
        while left < right:
            w=right-left
            h=min(height[left],height[right])
            curr_area=w*h
            area=max(area,curr_area)
            if height[right]>height[left]:
                left+=1
            else:
                right-=1
        return area