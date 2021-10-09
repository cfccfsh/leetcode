class Solution:
    def sort_list(self, target_list):
        if len(target_list) <= 1:
            return target_list

        middle = target_list[len(target_list) // 2]

        left_list = [item for item in target_list if item < middle]
        middle_list = [item for item in target_list if item == middle]
        right_list = [item for item in target_list if item > middle]

        return self.sort_list(left_list) + middle_list + self.sort_list(right_list)

    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        new_res = nums1[:m] + nums2[:n]
        res = self.sort_list(new_res)
        return res

    def merge2(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m - 1, n - 1
        tail = m + n - 1
        while p1 >= 0 or p2 >= 0:
            if p1 == -1:
                nums1[tail] = nums2[p2]
                p2 -= 1
            elif p2 == -1:
                nums1[tail] = nums1[p1]
                p1 -= 1
            elif nums1[p1] > nums2[p2]:
                nums1[tail] = nums1[p1]
                p1 -= 1
            else:
                nums1[tail] = nums2[p2]
                p2 -= 1
            tail -= 1



if __name__ == "__main__":
    a = [1,2,3,0,0,0]
    b = [2,5,6]

    m = len(a)
    n = len(b)
    s = Solution()
    cc = s.merge2(a,3,b,3)
    print(cc)
    print(a[:0])