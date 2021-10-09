# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
#
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
#
# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        res_l1 = []
        res_l2 = []
        res_l1.append(str(l1.val) if l1 else "0")
        res_l2.append(str(l2.val) if l2 else "0")
        while l1.next or l2.next:

            l1 = l1.next if l1.next else ListNode()
            l2 = l2.next if l2.next else ListNode()
            res_l1.append(str(l1.val) if l1 else "0")
            res_l2.append(str(l2.val) if l2 else "0")

        int_l1 = int("".join(res_l1[::-1]))
        int_l2 = int("".join(res_l2[::-1]))

        res = int_l1+int_l2

        node = ListNode()
        for item in range(len(str(res))):
            node.next = ListNode(int(str(res)[item]))

        return node.next

    def addTwoNumbers_v2(self, l1, l2):
        def sum_node(l1, l2, i):
            if not l1 and not l2 and not i:
                return

            s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + i
            i = s // 10
            node = ListNode(s % 10)
            node.next = sum_node(l1.next if l1 else None, l2.next if l2 else None, i)

            return node

        node = sum_node(l1, l2, 0)

        return node


a1 = ListNode(9)
a2 = ListNode(9)
a3 = ListNode(9)
a4 = ListNode(9)
a5 = ListNode(9)
a6 = ListNode(9)
a7 = ListNode(9)

b1 = ListNode(9)
b2 = ListNode(9)
b3 = ListNode(9)
b4 = ListNode(9)

a6.next = a7
a5.next = a6
a4.next = a5
a3.next = a4
a2.next = a3
a1.next = a2

b3.next = b4
b2.next = b3
b1.next = b2


# a1 = ListNode(0)
# b1 = ListNode(0)

s = Solution()
s.addTwoNumbers_v2(a1,b1)