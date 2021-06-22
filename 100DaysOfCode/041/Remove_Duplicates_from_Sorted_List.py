from linkedList import LinkedList

class Solution:
    def deleteDuplicates(self, head) :
        cur = head

        while cur:
            while cur.next and cur.next.data == cur.data:
                cur.next = cur.next.next  # skip duplicated node
            cur = cur.next  # not duplicate of current node, move to next node
        return head

llist = LinkedList()
llist.append(1)
llist.append(1)
llist.append(1)

llist.head = Solution().deleteDuplicates(llist.head)
llist.print_list()