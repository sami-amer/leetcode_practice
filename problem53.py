from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = maxSum = nums[0]

        for i in range(1,len(nums)):
            currSum = max(nums[i],currSum + nums[i])
            maxSum = max(currSum, maxSum)
        return maxSum



if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4] # output = 6
    print(Solution.maxSubArray(None,nums))