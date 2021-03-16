# 暂留
class Solution:
    def generateMatrix(self, n):
        if n == 1:
            return [[1]]

        row = n
        col = n - 2

        matrix = [[0 for i in range(n)] for i in range(n)]

        for i in range(n*n):
            if i < row:
                matrix[0][i] = i+1



if __name__ == '__main__':
    s = Solution()
    s.generateMatrix(4)
    # 1   2  3 4  5
    # 12 13 14 5  6
    # 11 16 15 6  7
    # 10 9  8  7  8
    # 10 9  11  10  9
