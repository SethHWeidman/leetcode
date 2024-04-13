import typing


class ListNode:
    def __init__(self, key: int, val: int = -1):
        self.key = key
        self.val = val
        self.next: ListNode = None
        self.prev: ListNode = None
