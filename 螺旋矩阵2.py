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
    dic = {"name": "zs", "age": 18, "city": "深圳", "tel": "1362626627"}

    dict_v2 = {v:k for k,v in dic.items()}

    print(dict_v2)

    print(sorted([1, 3, 7, 9] + [2, 2, 6, 8],reverse=False))


    class Solution:
        def searchBST(self, tree,value):
            if not tree:
                return None
            if tree.val == value:
                return tree
            if tree.val > value:
                return self.searchBST(tree.left, value)
            return self.searchBST(tree.right, value)
        
    a = dict()


    def generate():
        i = 0
        while i < 5:
            print("我在这。。")
            xx = yield i  # 注意，python程序，碰到=，都是先从右往左执行
            print(xx)
            i += 1


    g = generate()

    g.send(None)  # <==> next(g) 第一次启动，执行到yield i（此时i=0），挂起任务，主程序继续往下执行

    g.send("lalala")

    next(g)