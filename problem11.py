class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0 # We start by holding the left 
        right = len(height) - 1 # and right poles
        mx = 0
        curr_area = 0

        while left < right:
            if height[left] < height[right]:
                curr_area = min(height[left], height[right]) * (right - left)
                left += 1
            else:
                curr_area = min(height[left], height[right]) * (right - left)
                right -= 1
            mx = max(curr_area, mx)
        return mx






if __name__ == "__main__":
    input1 = [1,8,6,2,5,4,8,3,7]
    input2 = [1,3,2,5,25,24,5]
    input3 = [1,2,3,4,5,25,24,3,4]
    
    print(Solution.maxArea(None, input3))