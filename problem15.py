
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        results = []
        nums.sort()
        for i in range(len(nums) - 2): # - 2 because we want to stop when we run out of pairs of 3
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums) - 1
            
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0 : 
                    l += 1 
                elif s > 0:
                    r -= 1
                else: # This means we found an answer
                    results.append((nums[i],nums[l],nums[r]))
                    while l < r and nums [l] == nums [l+1]: # we need to avoid duplicates
                        l += 1
                    while l< r and nums[r] == nums[r-1]:
                        r -= 1
                    l+=1; r-=1 # we then move them one step
        return results






if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    print(Solution.threeSum(None,nums))