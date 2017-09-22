# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
     def traverse(self,ListNode):
         while(ListNode != None):
             print "Node", ListNode.val
             ListNode = ListNode.next

class Solution(object):
    def reverseList(self, head):

        if (head != None):
            if head.next == None:
                return head
            i = head.next
            j = i.next
            head.next = None
            if (j == None):
                i.next = head
                return i

            while (j.next != None):
                i.next = head
                head = i
                i = j
                j = j.next

            i.next = head
            j.next = i
            head = j

            return head
        else:
            return None
    def appendNode(self,head):
        if(head != None):
            n = ListNode(0)
            n.next = None
            n.val = head.val
            while(head.next != None):
                head = head.next
                n1 = ListNode(0)
                n1.val = head.val
                n1.next = n
                n = n1

        while(n != None):
            print n.val
            n = n.next

    def deleteNode(self,node):

        n1 = ListNode
        n1 = node.next
        node.val = n1.val
        node.next = n1.next

        del n1
        """
        :type head: ListNode
        :rtype: ListNode
        """
l1 = ListNode(2)
l2 = ListNode(3)
l3 = ListNode(4)
l4 = ListNode(5)
l5 = ListNode(6)
l1.next = l2
l2.next = l3
l3.next= l4
l4.next = l5
l5.next = None
#l1.traverse(l1)


s1 =Solution()
#s1.reverseList(l1)
s1.appendNode(l1)