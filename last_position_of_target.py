class Solution:
    # @param An integer array sorted in ascending order
    # @param An interger, the target
    # @return an integer, the index
    def lastPosition(self, alist, target):
        if not alist or target is None:
            return -1

        start = 0
        end = len(alist) - 1

        while start + 1 < end:
            mid = start + (end - start) / 2

            if alist[mid] < target:
                start = mid
            elfi alist[mid] > target:
                end = mid
            else:
                start = mid

        if alist[end] == target:
            return end
        elif alist[start] == target:
            return start
        else: return -1
