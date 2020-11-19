"""
Развернуть односвязный список (вернуть ссылку на новое начало списка). Реализовать итеративно и рекурсивно.
Пример: 1->2->3->4->5->None станет 5->4->3->2->1->None
"""


class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next


def reverse_recursive(head: ListNode):
    if head is None or head.next is None:
        # Пара не полная, разворачивать нечего
        return head

    tail = reverse_recursive(head.next)
    head.next.next = head
    head.next = None
    return tail


def reverse_iterative(head: ListNode):
    cur = None
    while head is not None:
        next, head.next = head.next, cur
        cur, head = head, next
    return cur


def reverse_extra_memory(head: ListNode):
    cur = None

    while head is not None:
        node = ListNode(head.val, cur)
        cur = node
        head = head.next

    return cur


def print_list(head: ListNode):
    while head is not None:
        print(head.val, end=" -> ")
        head = head.next
    print()


# Recursive Example
head = cur = ListNode()
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
    cur.next = ListNode(i)
    cur = cur.next
head = head.next

print_list(head)
new_head = reverse_recursive(head)
print_list(new_head)

# Iterative Example
head = cur = ListNode()
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
    cur.next = ListNode(i)
    cur = cur.next
head = head.next

print_list(head)
new_head = reverse_iterative(head)
print_list(new_head)

# Iterative Example
head = cur = ListNode()
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
    cur.next = ListNode(i)
    cur = cur.next
head = head.next

print_list(head)
new_head = reverse_extra_memory(head)
print_list(new_head)
