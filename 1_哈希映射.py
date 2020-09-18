class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]"""
        d={}
        n=len(nums)
        for x in range(n):
            if target-nums[x] in d:
                return  x,d[target-nums[x]]
            else:
                d[nums[x]]=x
