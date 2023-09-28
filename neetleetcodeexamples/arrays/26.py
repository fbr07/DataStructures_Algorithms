class Solution:
    def removeDuplicates(self, nums):
        leftpointer = 1
        for r in range(1, len(nums)):
            