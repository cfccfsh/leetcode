class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []

        if len(matrix) == 1:
            return matrix[0]
        else:
            if len(matrix[-1]) > 1:
                matrix[-1] = [matrix[-1][0]] + matrix[-1][1:-1][::-1] + [matrix[-1][-1]]

        new_list = [item for item in matrix[0]]

        head_list = []
        end_list = []

        middle_list = []

        for index,item in enumerate(matrix[1:]):
            if len(item) == 1:
                end_list.append(item[0])
            else:
                if item:
                    head_list.append(item[0])
                    end_list.append(item[-1])
                    middle_list.append(item[1:-1])


        middle_list = middle_list[::-1]
        res_list = new_list + end_list
        if middle_list:
            res_list += [item for item in middle_list[0]]
        head_list = head_list[::-1]
        middle_list = middle_list[1:][::-1]

        for index,x in enumerate(head_list):
            res_list += [head_list[index]]

        if middle_list:
            res_next = self.spiralOrder(middle_list)

            res_list += res_next

        return res_list

if __name__ == '__main__':
    # matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    # matrix = [[3],[2]]
    # matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    matrix = [[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]
    s = Solution()
    res = s.spiralOrder(matrix)
    print(res)