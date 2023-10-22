class Solution(object):
    def minSubArrayLen(self, target, nums):
        start = 0
        windowSum = 0
        #maximum possible length given constraints
        minlength = len(nums) + 1

        for end in range(len(nums)):
            windowSum+=nums[end]
            while windowSum >= target:
                minlength = min(minlength, end - start + 1)
                windowSum -= nums[start]
                start+=1

        if minlength > len(nums): return 0
            
        return minlength
        