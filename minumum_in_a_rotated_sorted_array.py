'''
A sorted array is rotated at some pivot unknown beforehand
EX: [0 1 2 3 4 5 6 ] might become [4 5 6 0 1 2 3]
Assume no duplicates
'''

class Solution:
    # @param: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, nums):
        if len(nums) == 0:
            return 0

        start, end = 0, len(nums) - 1
        target = nums[-1]
        while start + 1 < end:
            mid = (start + end) / 2
            if nums[mid] <= target:
                end = mid
            else:
                start = mid

        return min(nums[start], nums[end])
