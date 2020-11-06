"""
Дан связный список. Нужно попарно развернуть 2 соседних узла и вернуть новую ссылку на первый элемент.
Пример: 1 -> 2 -> 3 -> 4 станет 2 -> 1 -> 4 -> 3
"""


class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next


def swap_pairs_rec(head: ListNode) -> ListNode:
    if head == None or head.next == None:
        return head
    # 1 -> 2 -> ...
    first = head
    second = head.next

    # 1 -> swap_pairs_rec(second.next) = 4
    # 2 -> 1
    first.next = swap_pairs_rec(second.next)
    second.next = first

    return second


def swap_pairs_iter(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    new = ListNode(next=head)
    prev_node = new

    while head != None and head.next != None:
        first = head
        second = head.next

        # Swapping
        prev_node.next = second
        first.next = second.next
        second.next = first

        prev_node = first
        head = first.next

    return new.next


def print_list(head: ListNode):
    while head != None:
        print(head.val, end=" ")
        head = head.next
    print()


# Recursive Example
head = cur = ListNode()
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
    cur.next = ListNode(i)
    cur = cur.next
head = head.next

print_list(head)
new_head = swap_pairs_rec(head)
print_list(new_head)

# Iterative Example
print()
head = cur = ListNode()
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    cur.next = ListNode(i)
    cur = cur.next
head = head.next

print_list(head)
new_head = swap_pairs_iter(head)
print_list(new_head)
