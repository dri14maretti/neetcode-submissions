class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximumArea = 0
        l, r = 0, len(heights) - 1
        

        while l < r:
            width = r - l
            calcHeight = min(heights[l], heights[r])
            area = width * calcHeight
            maximumArea = max(area, maximumArea)

            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1

        return maximumArea