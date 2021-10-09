class Solution:
    def sort_nums(self,nums):
        if not nums:
            return []

        middle_params = nums[len(nums)//2]

        left_nums = [item for item in nums if item < middle_params]
        right_nums = [item for item in nums if item > middle_params]

        return self.sort_nums(left_nums) + [middle_params] + self.sort_nums(right_nums)

    def findMin(self, nums):
        if len(nums) == 1:
            return nums[0]
        nums = self.sort_nums(nums)

        return nums[0]


    def quick_sort(self,array,start,end):
        p = array[0]

        while start <= end:
            if array[start] > p and array[end] <= p:
                array[start],array[end] = array[end],array[start]

                start += 1

            elif array[start] <=p:
                start += 1
            elif array[end] >= p:
                end -= 1

    def quickSort(self,data, start, end):
        i = start
        j = end
        # i与j重合时，一次排序结束
        if i >= j:
            return
        # 设置最左边的数为基准值
        flag = data[start]
        while i < j:
            while i < j and data[j] >= flag:
                j -= 1
            # 找到右边第一个小于基准的数，赋值给左边i。此时左边i被记录在flag中
            data[i] = data[j]
            while i < j and data[i] <= flag:
                i += 1
            # 找到左边第一个大于基准的数，赋值给右边的j。右边的j的值和上面左边的i的值相同
            data[j] = data[i]
        # 由于循环以i结尾，循环完毕后把flag值放到i所在位置。
        data[i] = flag
        # 除去i之外两段递归
        self.quickSort(data, start, i - 1)
        self.quickSort(data, i + 1, end)

    def quick(self,array,start,end):
        p = array[start]

        i = start
        j = end

        if i >= j:
            return

        while i < j:
            while i < j and array[j] >= p:
                j -= 1
            array[i] = array[j]

            while i <j and array[i] <= p:
                i += 1
            array[j] = array[i]

        array[i] = p
        self.quick(array,start,i-1)
        self.quick(array,i+1,end)


if __name__ == '__main__':
    a = [9,25,8,9,15,93,69]
    s = Solution()
    s.quickSort(a,0,len(a)-1)