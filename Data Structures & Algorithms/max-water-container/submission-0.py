class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            # print(f"left is {left} and right is {right}")
            h = min(height[left],height[right])
            w = right - left
            # print(f"height is {h} and width is {w}")
            area = h * w
            if area > max_area:
                max_area = area
            # print(f"area is {area}")
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return max_area


        

        