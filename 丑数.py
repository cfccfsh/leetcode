class Solution:
    def isUgly(self, n):
        if n == 0:
            return False
        while n:
            if n == 1:
                return True

            if not n%2:
                n = n/2
            elif not n%3:
                n = n/3
            elif not n%5:
                n = n/5
            else:
                return False
        return True


if __name__ == '__main__':
    n = 14
    s = Solution()
    a = s.isUgly(n)
    print(a)