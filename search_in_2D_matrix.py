'''
search for a value in a m*n matrix

Matrix has following properties:
    *  Integers in each row sorted from left to right
    *  First integer of each row is greater than the last integer of the previous row

Example:
[
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
Given target = 3, return true.

'''

class Solution:
    '''
    @param: matrix, a list of lists of Integers
    @param: target, an integer
    @return: a boolean, indicate whether target in matrix
    '''
    def targetInMatrix(self, matrix, target):
        if len(matrix) == 0:
            return False
        n, m = len(matrix), len(matrix[0])
        start, end = 0, n * m -1
        while start + 1 < end:
            mid = (start + end) / 2
            x, y = mid /m, mid % m
            if matrix[x][y] < target:
                start = mid
            else:
                end = mid
            print(start, end)
        x, y = start / m, start % m
        if matrix[x][y] == target:
            return True
        x, y = end / m, end % m
        if matrix[x][y] == target:
            return True

        return False

s = Solution()
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]]
print(s.targetInMatrix(matrix, 34))
