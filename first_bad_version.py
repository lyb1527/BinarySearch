'''
First bad version is an integer from 1 to n. One day, someone committed
a bad version in the code base. It caused the following version to fail in the unit
unit test. Find the first bad version. Can use SVNRepo

EX:
Given n = 5:

isBadVersion(3) -> false
isBadVersion(5) -> true
isBadVersion(4) -> true
Here we are 100% sure that the 4th version is the first bad version.

'''

class Solution:
    #@param: an integer
    #@return : an integer which is the first value
    def firstBadVersion(self, n):
        start, end = 1, n
        while start + 1 < end:
            mid = (start + end) / 2
            if SVNRepo.isBadVersion(mid):
                end = mid
            else:
                start = mid
        if SVNRepo.isBadVersion(start):
            return start
        return end
