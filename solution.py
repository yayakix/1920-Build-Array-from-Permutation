class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for x in range(len(nums)):
            firstNum = nums[x]
            ans.append(nums[firstNum])
        return ans
