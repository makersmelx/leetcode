class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(self, head: ListNode) -> ListNode:
    if not head:
        return None
    write = True
    itr = head
    current = None
    ret_head = ListNode()
    ret_itr = ret_head
    while itr:
        if current is None:
            current = itr.val
        elif current == itr.val:
            write = False
        else:
            if write:
                ret_itr.next = ListNode(val=current)
                ret_itr = ret_itr.next
            write = True
            current = itr.val
        itr = itr.next
        
    if (write):
        ret_itr.next = ListNode(val=current)
    return ret_head.next


if __name__ == "__main__":
    case = ListNode(1, ListNode(2, ListNode(3, ListNode(
        3, ListNode(4, ListNode(4, ListNode(5, None)))))))

    deleteDuplicates(None, case)
