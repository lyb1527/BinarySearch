'''
Given a target number and an integer array A sorted in ascending order,
find the index i in A such that A[i] is closest to the given target
ASSUME: can be duplicates in the array,
EX:
Given [1, 2, 3] and target = 2, return 1.

Given [1, 4, 6] and target = 3, return 1.

Given [1, 4, 6] and target = 5, return 1 or 2.

Given [1, 3, 3, 4] and target = 2, return 0 or 1 or 2

'''


class Solution:
    def closestNumber(self, alist, target):
        if not alist or target is None:
            return -1
        start, end = 0, len(alist) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if alist[mid] == target:
                return mid
            elif alist[mid] > target:
                end = mid
            else:
                start = mid

        if alist[end] - target > target - alist[start]:
            return start
        else:
            return end
