'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1:ListNode, l2:ListNode):
        """
        :type l1: ListNode
        :type l2: ListNode
        :type: ListNode
        """
        head=ListNode(0)
        node=head
        carry=0
        while l1 or l2:
            x=l1.val if l1 else 0
            y=l2.val if l2 else 0
            sum=x+y+carry
            carry=sum//10
            node.next =ListNode(sum%10)
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
            node=node.next
        if carry!=0:
            node.next=ListNode(1)
        return head.next