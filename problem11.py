def calcArea(height, i,j):
    # print(i,j)
    return min(height[i], height[j]) * abs(j - i)

def maxArea(height):
    # O (N^2) solution
    # curr_max = 0
    # for i in range(len(height)):
    #     for j in range(1,len(height)):
    #         area = min(height[i], height[j]) * (j - i)
    #         curr_max = area if area > curr_max else curr_max
    # return curr_max
    ## The above times out in LC
    left = 0 # We start by holding the left 
    right = len(height) - 1 # and right poles
    maxes = set() # All our possible answers are here: we only need to return the maximum size possible
    maxes.add(calcArea(height,left,right))
    while left < right -1:
        if calcArea(height, left+1, right) > max(maxes) and calcArea(height, left, right - 1) > max(maxes):
            maxes.add(calcArea(height, left, right - 1))
            maxes.add(calcArea(height, left + 1, right))
            right -=1
            left += 1
        elif calcArea(height, left+1, right) > max(maxes):
            maxes.add(calcArea(height, left+1, right))
            left += 1
        elif calcArea(height, left, right - 1) > max(maxes):
            maxes.add(calcArea(height, left, right - 1))
            right -= 1
        else:
            maxes.add(maxArea(height[left+1:right]))
            maxes.add(maxArea(height[left:right - 1]))
            left+=1
            right-=1
    return max(maxes)





if __name__ == "__main__":
    input1 = [1,8,6,2,5,4,8,3,7]
    input2 = [1,3,2,5,25,24,5]
    input3 = [1,2,3,4,5,25,24,3,4]
    
    print(maxArea(input3))