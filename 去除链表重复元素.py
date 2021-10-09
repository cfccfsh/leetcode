# 存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除所有重复的元素，使每个元素 只出现一次 。
#
# 返回同样按升序排列的结果链表。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.res = set()

    def deleteDuplicates(self, head):
        if not head:
            return

        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head



a = ListNode(1)
b = ListNode(2)
c = ListNode(2)
d = ListNode(3)

c.next = d
b.next = c
a.next = b

s = Solution()
res = s.deleteDuplicates(a)
print(res)