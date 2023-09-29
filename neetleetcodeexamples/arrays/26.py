class Solution:
    def removeDuplicates(self, nums):
        left = 1  # starting at index one since index 0 will be unique already
        for i in range(
            1, len(nums)
        ):  # I have 1 starting because thats where we want to start in the 1st index position
            if nums[i] != nums[i - 1]:
                nums[left] = nums[i]
                left += 1
        return left

    removeDuplicates([1, 1, 2])
