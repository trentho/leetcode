from __future__ import annotations

from typing import Iterable

from .nodes import DoublyListNode, ListNode


def build_linked_list(values: Iterable[int]) -> ListNode | None:
    dummy = ListNode(0)
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def linked_list_to_list(head: ListNode | None) -> list[int]:
    out: list[int] = []
    cur = head
    while cur:
        out.append(cur.val)
        cur = cur.next
    return out


def print_linked_list(head: ListNode | None) -> None:
    vals = linked_list_to_list(head)
    print(" -> ".join(map(str, vals)) if vals else "<empty>")


def detect_cycle(head: ListNode | None) -> ListNode | None:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break
    else:
        return None

    start = head
    while start is not slow:
        start = start.next
        slow = slow.next

    return start


def build_doubly_linked_list(values: Iterable[int]) -> DoublyListNode | None:
    head: DoublyListNode | None = None
    prev: DoublyListNode | None = None

    for v in values:
        node = DoublyListNode(v)
        if head is None:
            head = node
        if prev is not None:
            prev.next = node
            node.prev = prev
        prev = node

    return head
