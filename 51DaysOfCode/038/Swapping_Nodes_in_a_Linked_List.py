from linkedList import LinkedList

class Solution:
    def swapNodes(self, head, k):
        length = 1
        curr = head
        while curr:
            curr = curr.next
            length += 1

        idx1 = length - k
        idx2 = k

        if idx1 == idx2:
            return head

        prev1 = prev2 = None
        curr1 = curr2 = head
        length = 1
        while curr1 and length != idx1:
            prev1 = curr1
            curr1 = curr1.next
            length += 1
        length = 1
        while curr2 and length != idx2:
            prev2 = curr2
            curr2 = curr2.next
            length += 1
        if prev1:
            prev1.next = curr2
        else:
            head = curr2

        if prev2:
            prev2.next = curr1
        else:
            head = curr1

        curr2.next, curr1.next = curr1.next, curr2.next

        return head

llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)

llist.head = Solution().swapNodes(llist.head, 3)
llist.print_list()