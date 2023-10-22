class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        mp = {}

        for index, num in enumerate(nums):

            find = target - num

            if find in mp:
                return {index, mp[find]}

            mp[num] = index